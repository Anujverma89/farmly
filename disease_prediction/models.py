from django.db import models

# Create your models here.

class Image(models.Model):
    crop_image=models.ImageField(upload_to='images/')
