from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    year_birth=models.IntegerField()

class Login(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class MealPlanner(models.Model):
    preparation=models.TimeField()

class ContactCenter(models.Model):
    issues=models.TextField(max_length=500, null=True, blank=True)



