from django.urls import re_path
from category_app.views import CategoryAPIView, CategoryRetrieveUpdateDestroyAPIView


urlpatterns = [

    # -----Apis for category list, create, delete and update-----
    re_path(r'category/(?P<pk>\d+)/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-curd"),
    re_path(r'category/', CategoryAPIView.as_view(), name="category-curd"),
]
