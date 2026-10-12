from django.db import models
from django.contrib.auth.models import AbstractUser
from persiantools.jdatetime import JalaliDateTime

def get_jalali_datetime_now_for_date_joined():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')


class CUser(AbstractUser):
    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    username = models.CharField(error_messages={'unique': 'یک کاربر با این نام وجود دارد.'}, max_length=150, verbose_name='username', unique=True)
    phone = models.CharField(max_length=16, verbose_name='phone', unique=True)
    date_joined = models.CharField(default=get_jalali_datetime_now_for_date_joined, max_length=50, verbose_name='date joined')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    def __str__(self):
        return self.username
