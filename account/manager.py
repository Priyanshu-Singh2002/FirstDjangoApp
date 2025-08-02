from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number,username, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number must be set')
        if not username:
            raise ValueError('The username is required.')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,username = username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number,username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number,username, email, password, **extra_fields)