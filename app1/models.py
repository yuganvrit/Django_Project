from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    grade = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    published_date = models.DateField()

    def __str__(self):
        return self.title
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='phone_numbers')

    def __str__(self):
        return self.phone_number


    

    