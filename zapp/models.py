from django.db import models
from django.contrib import auth

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.title
