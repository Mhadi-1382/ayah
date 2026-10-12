from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from auth_app.models import CUser
from main_app.models import Contactus
from .models import Surah, Doa, Ahadis, VasiatnamehShohada, ZiyartMajazi, DOA_CATEGORY, AppInstallers, WelcomeNotification
from .send_notify import config_notify

def panel(request):
    if not request.user.is_superuser:
        return redirect('/')
    return render(request, 'pages/panel/panel.html', {'surah': Surah.objects.all(), 'doa': Doa.objects.all(), 'categories': DOA_CATEGORY, 'ahadis': Ahadis.objects.all(), 'ziyartMajazi': ZiyartMajazi.objects.all(), 'vasiatnamehShohada': VasiatnamehShohada.objects.all(), 'users': CUser.objects.all(), 'contactus': Contactus.objects.all(), 'installers': AppInstallers.objects.all(), 'welcomeNotification': WelcomeNotification.objects.all()})


def user_disable(request, user_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            user = get_object_or_404(CUser, id=user_id)
            try:
                user.is_active = False
                user.save()

                messages.success(request, 'کاربر «{0}» با موفقیت غیرفعال شد.'.format(user_id))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'غیرفعال سازی کاربر «{0}» با مشکل مواجه شد.'.format(user_id))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def user_enable(request, user_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            user = get_object_or_404(CUser, id=user_id)
            try:
                user.is_active = True
                user.save()

                messages.success(request, 'کاربر «{0}» با موفقیت فعال شد.'.format(user_id))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'فعال سازی کاربر «{0}» با مشکل مواجه شد.'.format(user_id))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def user_remove(request, user_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            user = get_object_or_404(CUser, id=user_id)
            try:
                user.delete()

                messages.success(request, 'کاربر «{0}» با موفقیت حذف شد.'.format(user_id))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'حذف کاربر «{0}» با مشکل مواجه شد.'.format(user_id))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')


def contact_us_remove(request, contact_us_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            contact_us = get_object_or_404(Contactus, id=contact_us_id)
            try:
                contact_us.delete()

                messages.success(request, 'محتوای مورد نظر با موفقیت حذف شد.')
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'حذف محتوای مورد نظر با مشکل مواجه شد.')
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')


def surah_add(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            surahNameFa = request.POST.get('surahNameFa')
            surahNameAr = request.POST.get('surahNameAr')
            surahFullText = request.POST.get('surahFullText')
            surahFullTranslate = request.POST.get('surahFullTranslate')
            surahFullTafsir = request.POST.get('surahFullTafsir')
            quriName = request.POST.get('quriName')
            numberAyeh = request.POST.get('numberAyeh')
            surahSound = request.FILES.get('surahSound')

            try:
                Surah.objects.create(
                    surah_name_fa = surahNameFa,
                    surah_name_ar = surahNameAr,
                    surah_full_text = surahFullText,
                    surah_full_translate = surahFullTranslate,
                    surah_full_tafsir = surahFullTafsir,
                    quri_name = quriName,
                    number_ayeh = numberAyeh,
                    surah_sound = surahSound,
                )

                messages.success(request, 'سوره «{0}» با موفقیت ایجاد شد.'.format(surahNameFa))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ایجاد سوره «{0}» با مشکل مواجه شد.'.format(surahNameFa))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def surah_edit(request, surah_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            surahNameFa = request.POST.get('surahNameFaForEdit')
            surahNameAr = request.POST.get('surahNameArForEdit')
            surahFullText = request.POST.get('surahFullTextForEdit')
            surahFullTranslate = request.POST.get('surahFullTranslateForEdit')
            surahFullTafsir = request.POST.get('surahFullTafsirForEdit')
            quriName = request.POST.get('quriNameForEdit')
            numberAyeh = request.POST.get('numberAyehForEdit')
            surahSound = request.FILES.get('surahSoundForEdit')

            surah = get_object_or_404(Surah, id=surah_id)
            try:
                surah.surah_name_fa = surahNameFa
                surah.surah_name_ar = surahNameAr
                surah.surah_full_text = surahFullText
                surah.surah_full_translate = surahFullTranslate
                surah.surah_full_tafsir = surahFullTafsir
                surah.quri_name = quriName
                surah.number_ayeh = numberAyeh
                surah.surah_sound = surahSound
                surah.save()

                messages.success(request, 'سوره «{0}» با موفقیت ویرایش شد.'.format(surahNameFa))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ویرایش سوره «{0}» با مشکل مواجه شد.'.format(surahNameFa))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def surah_remove(request, surah_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            surah = get_object_or_404(Surah, id=surah_id)
            try:
                surah.delete()

                messages.success(request, 'سوره مورد نظر با موفقیت حذف شد.')
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'حذف سوره مورد نظر با مشکل مواجه شد.')
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')


def doa_add(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            doaName = request.POST.get('doaName')
            doaFullTextTranslate = request.POST.get('doaFullTextTranslate')
            quriName = request.POST.get('quriName')
            doaCategory = request.POST.get('doaCategory')
            doaSound = request.FILES.get('doaSound')

            try:
                Doa.objects.create(
                    doa_name = doaName,
                    doa_full_text_translate = doaFullTextTranslate,
                    quri_name = quriName,
                    doa_category = doaCategory,
                    doa_sound = doaSound,
                )

                messages.success(request, 'دعای «{0}» با موفقیت ایجاد شد.'.format(doaName))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ایجاد دعای «{0}» با مشکل مواجه شد.'.format(doaName))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def doa_edit(request, doa_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            doaName = request.POST.get('doaNameForEdit')
            doaFullTextTranslateForEdit = request.POST.get('doaFullTextTranslateForEdit')
            quriName = request.POST.get('quriNameForEdit')
            doaCategory = request.POST.get('doaCategoryForEdit')
            doaSound = request.FILES.get('doaSoundForEdit')

            doa = get_object_or_404(Doa, id=doa_id)
            try:
                doa.doa_name = doaName
                doa.doa_full_text_translate = doaFullTextTranslateForEdit
                doa.quri_name = quriName
                doa.doa_category = doaCategory
                doa.doa_sound = doaSound
                doa.save()

                messages.success(request, 'دعای «{0}» با موفقیت ویرایش شد.'.format(doaName))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ویرایش دعای «{0}» با مشکل مواجه شد.'.format(doaName))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def doa_remove(request, doa_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            doa = get_object_or_404(Doa, id=doa_id)
            try:
                doa.delete()

                messages.success(request, 'دعا مورد نظر با موفقیت حذف شد.')
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'حذف دعا مورد نظر با مشکل مواجه شد.')
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')


def ahadis_add(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            ahadisTitle = request.POST.get('ahadisTitle')
            ahadisTextArForEdit = request.POST.get('ahadisTextAr')
            ahadisTextTranslate = request.POST.get('ahadisTextTranslate')
            ahadisSource = request.POST.get('ahadisSource')

            try:
                Ahadis.objects.create(
                    ahadis_title = ahadisTitle,
                    ahadis_text_ar = ahadisTextArForEdit,
                    ahadis_text_translate = ahadisTextTranslate,
                    ahadis_source = ahadisSource,
                )

                messages.success(request, 'حدیث «{0}» با موفقیت ایجاد شد.'.format(ahadisTitle))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ایجاد حدیث «{0}» با مشکل مواجه شد.'.format(ahadisTitle))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def ahadis_edit(request, ahadis_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            ahadisTitle = request.POST.get('ahadisTitleForEdit')
            ahadisTextArForEdit = request.POST.get('ahadisTextArForEdit')
            ahadisTextTranslate = request.POST.get('ahadisTextTranslateForEdit')
            ahadisSource = request.POST.get('ahadisSourceForEdit')

            ahadis = get_object_or_404(Ahadis, id=ahadis_id)
            try:
                ahadis.ahadis_title = ahadisTitle
                ahadis.ahadis_text_ar = ahadisTextArForEdit
                ahadis.ahadis_text_translate = ahadisTextTranslate
                ahadis.ahadis_source = ahadisSource
                ahadis.save()

                messages.success(request, 'حدیث «{0}» با موفقیت ویرایش شد.'.format(ahadisTitle))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ویرایش حدیث «{0}» با مشکل مواجه شد.'.format(ahadisTitle))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def ahadis_remove(request, ahadis_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            ahadis = get_object_or_404(Ahadis, id=ahadis_id)
            try:
                ahadis.delete()

                messages.success(request, 'حدیث مورد نظر با موفقیت حذف شد.')
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'حذف حدیث مورد نظر با مشکل مواجه شد.')
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')


def ziyart_majazi_add(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            ziyartMajaziTitle = request.POST.get('ziyartMajaziTitle')
            ziyartMajaziImg = request.FILES.get('ziyartMajaziImg')
            ziyartMajaziLink = request.POST.get('ziyartMajaziLink')

            try:
                ZiyartMajazi.objects.create(
                    ziyart_majazi_title = ziyartMajaziTitle,
                    ziyart_majazi_img = ziyartMajaziImg,
                    ziyart_majazi_link = ziyartMajaziLink,
                )

                messages.success(request, 'زیارتگاه «{0}» با موفقیت ایجاد شد.'.format(ziyartMajaziTitle))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ایجاد زیارتگاه «{0}» با مشکل مواجه شد.'.format(ziyartMajaziTitle))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def ziyart_majazi_edit(request, ziyart_majazi_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            ziyartMajaziTitle = request.POST.get('ziyartMajaziTitleForEdit')
            ziyartMajaziImg = request.FILES.get('ziyartMajaziImgForEdit')
            ziyartMajaziLink = request.POST.get('ziyartMajaziLinkForEdit')

            ziyart_majazi = get_object_or_404(ZiyartMajazi, id=ziyart_majazi_id)
            try:
                ziyart_majazi.ziyart_majazi_title = ziyartMajaziTitle
                ziyart_majazi.ziyart_majazi_img = ziyartMajaziImg
                ziyart_majazi.ziyart_majazi_link = ziyartMajaziLink
                ziyart_majazi.save()

                messages.success(request, 'زیارتگاه «{0}» با موفقیت ویرایش شد.'.format(ziyartMajaziTitle))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ویرایش زیارتگاه «{0}» با مشکل مواجه شد.'.format(ziyartMajaziTitle))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def ziyart_majazi_remove(request, ziyart_majazi_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            ziyart_majazi = get_object_or_404(ZiyartMajazi, id=ziyart_majazi_id)
            try:
                ziyart_majazi.delete()

                messages.success(request, 'زیارتگاه مورد نظر با موفقیت حذف شد.')
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'حذف زیارتگاه مورد نظر با مشکل مواجه شد.')
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')


def vasiatnameh_shohada_add(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            vasiatnamehShohadaName = request.POST.get('vasiatnamehShohadaName')
            vasiatnamehShohadaImg = request.FILES.get('vasiatnamehShohadaImg')
            vasiatnamehShohadaText = request.POST.get('vasiatnamehShohadaText')

            try:
                VasiatnamehShohada.objects.create(
                    vasiatnameh_shohada_name = vasiatnamehShohadaName,
                    vasiatnameh_shohada_img = vasiatnamehShohadaImg,
                    vasiatnameh_shohada_text = vasiatnamehShohadaText,
                )

                messages.success(request, 'وصیتنامه «{0}» با موفقیت ایجاد شد.'.format(vasiatnamehShohadaName))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ایجاد وصیتنامه «{0}» با مشکل مواجه شد.'.format(vasiatnamehShohadaName))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def vasiatnameh_shohada_edit(request, vasiatnameh_shohada_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            vasiatnamehShohadaName = request.POST.get('vasiatnamehShohadaNameForEdit')
            vasiatnamehShohadaImg = request.FILES.get('vasiatnamehShohadaImgForEdit')
            vasiatnamehShohadaText = request.POST.get('vasiatnamehShohadaTextForEdit')

            vasiatnameh_shohada = get_object_or_404(VasiatnamehShohada, id=vasiatnameh_shohada_id)
            try:
                vasiatnameh_shohada.vasiatnameh_shohada_name = vasiatnamehShohadaName
                vasiatnameh_shohada.vasiatnameh_shohada_img = vasiatnamehShohadaImg
                vasiatnameh_shohada.vasiatnameh_shohada_text = vasiatnamehShohadaText
                vasiatnameh_shohada.save()

                messages.success(request, 'وصیتنامه «{0}» با موفقیت ویرایش شد.'.format(vasiatnamehShohadaName))
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ویرایش وصیتنامه «{0}» با مشکل مواجه شد.'.format(vasiatnamehShohadaName))
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def vasiatnameh_shohada_remove(request, vasiatnameh_shohada_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            vasiatnameh_shohada = get_object_or_404(VasiatnamehShohada, id=vasiatnameh_shohada_id)
            try:
                vasiatnameh_shohada.delete()

                messages.success(request, 'وصیتنامه مورد نظر با موفقیت حذف شد.')
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'حذف وصیتنامه مورد نظر با مشکل مواجه شد.')
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')


def welcome_notification_edit(request, welcome_notification_id):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            welcomeNotificationText = request.POST.get('welcomeNotificationText')

            welcome_notification = get_object_or_404(WelcomeNotification, id=welcome_notification_id)
            try:
                welcome_notification.text_message = welcomeNotificationText
                welcome_notification.save()

                messages.success(request, 'متن پیام خوشآمد با موفقیت ویرایش شد.')
                return redirect('panel')
            except Exception as e:
                messages.error(request, 'ویرایش متن پیام خوشآمد با مشکل مواجه شد.')
                return redirect('panel')
        else:
            return redirect('/')
    else:
        return redirect('/')

def send_notify(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('sendNotifyTitle')
            content = request.POST.get('sendNotifyContent')
            icon = request.POST.get('sendNotifyIcon')
            link = request.POST.get('sendNotifyDeepLink')

            config_notify(title=title, content=content, icon=icon, link=link)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')
