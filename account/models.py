from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager  # Adjust import path if needed

class CustomUser(AbstractUser):
    username = None  # Disable the username field
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile/")

    USERNAME_FIELD = 'phone_number'    # Here, you can select those fields from which you want to signin
    REQUIRED_FIELDS = []  # Optional: add email as required

    objects = CustomUserManager()    # type: ignore
