from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response

from category_app.models import Category
from category_app.serializers import CategorySerializer
from category_app import task


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category.
    """
    queryset = Category.objects.filter(is_active=True).order_by('name')
    serializer_class = CategorySerializer


class CategoryAPIView(ListCreateAPIView):
    """
    For creating category and listing categories.
    """
    queryset = Category.objects.filter(is_active=True).order_by("name")
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Call independent task with category argument and countdown. It will run in 15 min and expire in 20 min.
        task.send_updation.apply_async([request.data.get("name")], countdown=900, expires=1200)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


