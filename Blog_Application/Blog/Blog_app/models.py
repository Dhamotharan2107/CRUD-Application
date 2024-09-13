from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')


    def __str__(self):
        return self.title
