from django.db import models
from auth_app.models import CUser
from persiantools.jdatetime import JalaliDateTime

def get_jalali_datetime_now_for_date_created_in_notes():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_bookmarks():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_contactus():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')


class Notes(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(CUser, on_delete=models.CASCADE, related_name='notes')
    title_note = models.CharField(max_length=500, verbose_name='title note')
    text_note = models.TextField(verbose_name='text note')
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_notes, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.title_note

class Bookmarks(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(CUser, on_delete=models.CASCADE, related_name='bookmarks')
    title_bookmark = models.CharField(max_length=500, verbose_name='title bookmark')
    link_bookmark = models.TextField(verbose_name='link bookmark')
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_bookmarks, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.title_bookmark

class Contactus(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(max_length=150, verbose_name='username')
    phone = models.CharField(max_length=16, verbose_name='phone')
    email = models.CharField(max_length=254, verbose_name='email')
    message = models.TextField(verbose_name='message', null=True)
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_contactus, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.username
