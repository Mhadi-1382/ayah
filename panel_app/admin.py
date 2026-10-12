from django.contrib import admin
from .models import Surah, Doa, Ahadis, VasiatnamehShohada, ZiyartMajazi, AppInstallers, WelcomeNotification

admin.site.register(Surah)
admin.site.register(Doa)
admin.site.register(Ahadis)
admin.site.register(VasiatnamehShohada)
admin.site.register(ZiyartMajazi)
admin.site.register(AppInstallers)
admin.site.register(WelcomeNotification)
