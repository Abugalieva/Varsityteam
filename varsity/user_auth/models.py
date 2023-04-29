from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(null=False, unique=True, max_length=80)
    # password = models.CharField(null=False, max_length=10)
    first_name = models.CharField(null=True, max_length=80, default='Name')
    last_name = models.CharField(null=True, max_length=255, default='Surname')
    email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_company = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ResetPassword(models.Model):
    email = models.EmailField(null=False, blank=False, max_length=255)
    token = models.CharField(null=False, blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    
class Coupon(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now_add=True)
