from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=20)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # You should hash the password
    gender = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.username