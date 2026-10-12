from django.urls import path
from api_app import views

urlpatterns = [
    path('get_app_installers/', view=views.get_app_installers, name='get_app_installers'),

    path('welcome_notification/', view=views.welcome_notification, name='welcome_notification'),

    path('surah/', view=views.surah, name='surah'),

    path('doa/', view=views.doa, name='doa'),

    path('ahadis/', view=views.ahadis, name='ahadis'),

    path('ziyart_majazi/', view=views.ziyart_majazi, name='ziyart_majazi'),

    path('vasiatnameh_shohada/', view=views.vasiatnameh_shohada, name='vasiatnameh_shohada'),
]
