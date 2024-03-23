from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    slug = models.SlugField()
    order = models.BooleanField(default = 0)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = True, auto_now = False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class CategoryImage(models.Model):
    title = models.CharField(max_length = 150, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "category")
    image = models.ImageField(upload_to='category/image')
    slug = models.SlugField()
    featured_image = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Category Image'

    def __str__(self):
        return self.title

