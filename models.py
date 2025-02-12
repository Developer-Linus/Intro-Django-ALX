# Models are defined as Python classes inheriting from django.db.models.Model base class.
# Each attribute in a model represents database field, and its data type is defined using field classes by Django.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    
    