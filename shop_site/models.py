from django.db import models

# Create your models here.
class Slider(models.model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()