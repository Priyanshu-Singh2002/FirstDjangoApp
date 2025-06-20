from django.db import models

# Create your models here.
#whenever you create a model or do any changes you have to run the command # python manage.py makemigrations
# and then python manage.py migrate to apply the changes to the database
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank = True)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    DOB = models.DateField()
    gender = models.CharField(max_length=1,choices=[('M','Male'),('F','Female'),('O','Other')],default='N')


