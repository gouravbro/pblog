from django.db import models
from django.contrib.auth.models import User
import time
from django.urls import reverse
from datetime import date
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    today = models.DateTimeField(auto_now_add=True)
    # hi = models.CharField(max_length=250)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')