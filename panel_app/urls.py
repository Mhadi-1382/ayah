from django.urls import path
from panel_app import views

urlpatterns = [
    path('panel/', view=views.panel, name='panel'),

    path('panel/user_disable/<int:user_id>/', view=views.user_disable, name='panel_user_disable'),
    path('panel/user_enable/<int:user_id>/', view=views.user_enable, name='panel_user_enable'),
    path('panel/user_remove/<int:user_id>/', view=views.user_remove, name='panel_user_remove'),

    path('panel/contact_us_remove/<int:contact_us_id>/', view=views.contact_us_remove, name='panel_contact_us_remove'),

    path('panel/surah_add/', view=views.surah_add, name='panel_surah_add'),
    path('panel/surah_edit/<int:surah_id>/', view=views.surah_edit, name='panel_surah_edit'),
    path('panel/surah_remove/<int:surah_id>/', view=views.surah_remove, name='panel_surah_remove'),

    path('panel/doa_add/', view=views.doa_add, name='panel_doa_add'),
    path('panel/doa_edit/<int:doa_id>/', view=views.doa_edit, name='panel_doa_edit'),
    path('panel/doa_remove/<int:doa_id>/', view=views.doa_remove, name='panel_doa_remove'),

    path('panel/ahadis_add/', view=views.ahadis_add, name='panel_ahadis_add'),
    path('panel/ahadis_edit/<int:ahadis_id>/', view=views.ahadis_edit, name='panel_ahadis_edit'),
    path('panel/ahadis_remove/<int:ahadis_id>/', view=views.ahadis_remove, name='panel_ahadis_remove'),

    path('panel/ziyart_majazi_add/', view=views.ziyart_majazi_add, name='panel_ziyart_majazi_add'),
    path('panel/ziyart_majazi_edit/<int:ziyart_majazi_id>/', view=views.ziyart_majazi_edit, name='panel_ziyart_majazi_edit'),
    path('panel/ziyart_majazi_remove/<int:ziyart_majazi_id>/', view=views.ziyart_majazi_remove, name='panel_ziyart_majazi_remove'),

    path('panel/vasiatnameh_shohada_add/', view=views.vasiatnameh_shohada_add, name='panel_vasiatnameh_shohada_add'),
    path('panel/vasiatnameh_shohada_edit/<int:vasiatnameh_shohada_id>/', view=views.vasiatnameh_shohada_edit, name='panel_vasiatnameh_shohada_edit'),
    path('panel/vasiatnameh_shohada_remove/<int:vasiatnameh_shohada_id>/', view=views.vasiatnameh_shohada_remove, name='panel_vasiatnameh_shohada_remove'),

    path('panel/welcome_notification/edit/<int:welcome_notification_id>/', view=views.welcome_notification_edit, name='panel_welcome_notification_edit'),
    path('panel/send_notify/', view=views.send_notify, name='send_notify'),
]
