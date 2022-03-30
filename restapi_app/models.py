from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):

    username = models.CharField(max_length=100,null=True,unique=True)
    password = models.CharField(max_length=100,null=True,unique=True)
    email = models.EmailField(max_length=100,null=True,unique=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=100,null=True)
    country =models.CharField(max_length=100,null=True)
    DOB = models.CharField(max_length=100,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['create','username']
    def get_username(self):
     return self.email

