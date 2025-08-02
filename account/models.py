from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager  # Adjust import path if needed

class CustomUser(AbstractUser):
    username = models.CharField(null=True,blank=True)  # Disable the username field
    phone_number = models.CharField(max_length=20, unique=True,null=False,blank=False)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile/")

    USERNAME_FIELD = 'phone_number'    # Here, you can select those fields from which you want to signin
    REQUIRED_FIELDS = ['username']  # Optional: add email as required

    objects = CustomUserManager()    # type: ignore
