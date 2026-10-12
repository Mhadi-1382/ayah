from django.urls import path
from main_app import views

urlpatterns = [
    path('', view=views.index, name='index'),

    path('search/', view=views.search, name='search'),

    path('contactus/', view=views.contact_us, name='contact_us'),

    path('surah/', view=views.surah, name='surah'),
    path('surah/<int:surah_id>/', view=views.surah_details, name='surah_details_slug'),
    
    path('doa/', view=views.doa, name='doa'),
    path('doa/<int:doa_id>/', view=views.doa_details, name='doa_details_slug'),
    path('doa/daily-prayers-ramadan/', view=views.doa_daily_prayers_ramadan, name='doa_daily_prayers_ramadan'),

    path('ahadis/', view=views.ahadis, name='ahadis'),

    path('ziyart_majazi/', view=views.ziyart_majazi, name='ziyart_majazi'),
    
    path('vasiatnameh_shohada/', view=views.vasiatnameh_shohada, name='vasiatnameh_shohada'),
    path('vasiatnameh_shohada/<int:vasiatnameh_shohada_id>/', view=views.vasiatnameh_shohada_details, name='vasiatnameh_shohada_details_slug'),
    
    path('note/add/', view=views.note_add, name='note_add'),
    path('note/edit/<int:note_id>/', view=views.note_edit, name='note_edit'),
    path('note/remove/<int:note_id>/', view=views.note_remove, name='note_remove'),
    
    path('bookmark/add/', view=views.bookmark_add, name='bookmark_add'),
    path('bookmark/remove/<int:bookmark_id>/', view=views.bookmark_remove, name='bookmark_remove'),
]
