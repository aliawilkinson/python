from tokenize import Name
from django.db import models

class Pet(models.Model):
    GENDER_CHOICES = [('F','Female'),('M','Male'),('O','Other')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(GENDER_CHOICES, blank=True)
    submissiondate = models.DateTimeField()
    age = models.IntegerField(null=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    vaccinations = models.ManyToManyField('Vaccine',blank=True)