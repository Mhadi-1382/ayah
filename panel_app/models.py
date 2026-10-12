from django.db import models
from persiantools.jdatetime import JalaliDateTime
from ckeditor.fields import RichTextField

def get_jalali_datetime_now_for_date_created_in_surah():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_doa():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_ahadis():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_ziyart_majazi():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_vasiatnameh_shohada():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_app_installers():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')
def get_jalali_datetime_now_for_date_created_in_welcome_notification():
    return JalaliDateTime.now().strftime('%Y-%m-%d %H:%M')

DOA_CATEGORY = [
    ('Doa', 'دعا'),
    ('Ziyart', 'زیارت')
]


class Surah(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    surah_name_fa = models.CharField(max_length=150, verbose_name='surah name fa')
    surah_name_ar = models.CharField(max_length=150, verbose_name='surah name ar')
    surah_full_text = RichTextField()
    surah_full_translate = RichTextField()
    surah_full_tafsir = RichTextField()
    quri_name = models.CharField(max_length=150, verbose_name='quri name')
    surah_sound = models.FileField(upload_to='audios/surah/' , verbose_name='surah sound')
    number_ayeh = models.CharField(max_length=254, verbose_name='number ayeh')
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_surah, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.surah_name_fa

class Doa(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    doa_name = models.CharField(max_length=150, verbose_name='doa name')
    doa_full_text_translate = RichTextField()
    quri_name = models.CharField(max_length=150, verbose_name='quri name')
    doa_sound = models.FileField(upload_to='audios/doa/' , verbose_name='doa sound')
    doa_category = models.CharField(max_length=150, choices=DOA_CATEGORY, verbose_name='doa category')
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_doa, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.doa_name

class Ahadis(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    ahadis_title = models.CharField(max_length=150, verbose_name='ahadis title')
    ahadis_text_ar = RichTextField()
    ahadis_text_translate = RichTextField()
    ahadis_source = models.CharField(max_length=300, verbose_name='ahadis source')
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_ahadis, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.ahadis_title

class ZiyartMajazi(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    ziyart_majazi_title = models.CharField(max_length=150, verbose_name='ziyart majazi title')
    ziyart_majazi_img = models.FileField(upload_to='imgs/ziyart_majazi/', verbose_name='ziyart majazi img')
    ziyart_majazi_link = models.TextField(verbose_name='ziyart majazi link')
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_ziyart_majazi, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.ziyart_majazi_title

class VasiatnamehShohada(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    vasiatnameh_shohada_name = models.CharField(max_length=150, verbose_name='vasiatnameh shohada name')
    vasiatnameh_shohada_img = models.FileField(upload_to='imgs/vasiatnameh_shohada/', verbose_name='vasiatnameh shohada img')
    vasiatnameh_shohada_text = RichTextField()
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_vasiatnameh_shohada, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.vasiatnameh_shohada_name

class AppInstallers(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    os = models.CharField(max_length=50, verbose_name='os')
    app_install_date = models.CharField(default=get_jalali_datetime_now_for_date_created_in_app_installers, max_length=50, verbose_name='app installers date')

    def __str__(self):
        return self.os

class WelcomeNotification(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    text_message = models.TextField(verbose_name='text message')
    date_created = models.CharField(default=get_jalali_datetime_now_for_date_created_in_welcome_notification, max_length=50, verbose_name='date created')

    def __str__(self):
        return self.text_message
