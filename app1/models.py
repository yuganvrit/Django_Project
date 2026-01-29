from django.db import models

# Create your models here.
class Teacher(models.Model):
    #construction jastai models le gareko
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=256)
    district_code=models.PositiveIntegerField()

    def __str__(self):
        return self.name
       