from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fullname = models.CharField(verbose_name='نام و نام خانوادگی', null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='ایمیل کاربر')
    phone_number = models.CharField(max_length=20, unique=True, verbose_name='تلفن همراه')
    parent_email = models.EmailField(verbose_name='ایمیل والد')


class Meta:
    model = CustomUser
    fields = ['fullname', 'username', 'email', 'phone_number', 'parent_email', 'password']


def __str__(self):
    return self.email or self.username
