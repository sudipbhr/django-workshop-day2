from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=255)
    image2  = models.ImageField(upload_to='blogs/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)