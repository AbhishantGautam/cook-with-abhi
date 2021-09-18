from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    ingredients = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()

    def __str__(self):
        return self.title