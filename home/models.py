from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Car(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    mileage = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    

@receiver(post_save,sender = Car)
def Know_Your_Car_Speed(sender,instance,**kwargs):
    print("Object Created And Saved Successfully..")
    print(sender,instance,kwargs)
