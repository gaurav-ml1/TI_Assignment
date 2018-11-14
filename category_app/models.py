from django.db import models
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.size
    limit_kb = 512 * 1024
    if file_size > limit_kb:
        raise ValidationError("Please upload image less then %s KB" % (limit_kb/1024))


class Category(models.Model):
    """
    Category model stored all categories with parent category.
    """
    parent = models.ForeignKey('self', blank=True, null=True, related_name="parent_category", help_text="Main category",
                               on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    description = models.TextField(help_text="Category description")
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="category", null=True, blank=True, max_length=100, validators=[validate_image])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Stringify return model object.
        :return: It return category name with parent if it is.
        """
        return "{}".format(self.name) if not self.parent else "{} (p)".format(self.name)

