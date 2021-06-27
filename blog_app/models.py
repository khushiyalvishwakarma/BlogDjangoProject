from django.db import models

# Create your models here.
from django.db import models

class bloglistmdl(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    task=models.TextField()

