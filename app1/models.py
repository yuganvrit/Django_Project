from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    grade = models.PositiveSmallIntegerField()


    def __str__(self):
        
        return self.name
    

    @property
    def is_adult(self):
        return self.age >= 18
    

    def save(self, *args, **kwargs): # new_fields)
        if self.age < 5:
            raise ValidationError("Age must be greater than 5")
        super().save(*args, **kwargs)
    


 

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


# first_author = Author.objects.first()
# get_all_books = Book.objects.filter(author=first_author)


# get_all_books =first_author.books.all()




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
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='teachers')



    def __str__(self):
        return self.name



class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    class_teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE,related_name='classroom')


    def __str__(self):
        return self.name




#Assignment 

#create restful apis for student teacher and course for crud operation 
#relation will be like student will have course rreference meaning one student
#can be enrolled in multiple courses and 
#and one teacher can in only one course 
#create models serializer and function based veiws
    




    



    

    