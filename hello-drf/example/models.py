from operator import mod
from pydoc import describe
from statistics import mode
from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()
