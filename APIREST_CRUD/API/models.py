from django.db import models

# Create your models here.


class Student (models.Model):
    name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    Average = models.FloatField()
    description = models.CharField(max_length=200)
    scholarship = models.CharField(max_length=200)

   