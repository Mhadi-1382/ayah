from django.shortcuts import redirect
from django.http import JsonResponse
from panel_app.models import AppInstallers, WelcomeNotification, Surah, Doa, Ahadis, ZiyartMajazi, VasiatnamehShohada
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit
import json

@csrf_exempt
@ratelimit(key='ip', rate='5/m', block=True)
def get_app_installers(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            os = data.get('os')
            if not os:
                return JsonResponse({'error': 'OS are required.'}, status=400)
            elif os == 'Windows' or os == 'Android':
                installers = AppInstallers.objects.create(os=os)
                return JsonResponse({'msg': 'OK', 'id': installers.id, 'os': installers.os, 'date': installers.app_install_date}, status=201)
            else:
                return JsonResponse({'error': 'Invaid OS type.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invaid JSON.'}, status=400)
    else:
        return redirect('/')


def welcome_notification(request):
    count = WelcomeNotification.objects.count()
    if count == 0:
        return JsonResponse({'error': []})
    else:
        welcome_notification = WelcomeNotification.objects.all()
        data = []
        for wn in welcome_notification:
            data.append({
                'id': wn.id,
                'text_message': wn.text_message,
                'date_created': wn.date_created,
            })
        return JsonResponse(data, safe=False)


def surah(request):
    count = Surah.objects.count()
    if count == 0:
        return JsonResponse({'error': []})
    else:
        surah = Surah.objects.all()
        data = []
        for s in surah:
            data.append({
                'id': s.id,
                'surah_name_fa': s.surah_name_fa,
                'surah_name_ar': s.surah_name_ar,
                'surah_full_text': s.surah_full_text,
                'surah_full_translate': s.surah_full_translate,
                'surah_full_tafsir': s.surah_full_tafsir,
                'quri_name': s.quri_name,
                'number_ayeh': s.number_ayeh,
                'surah_sound': f'{request.scheme}://{request.get_host()}/media/' + str(s.surah_sound),
                'date_created': s.date_created,
            })
        return JsonResponse(data, safe=False)


def doa(request):
    count = Doa.objects.count()
    if count == 0:
        return JsonResponse({'error': []})
    else:
        doa = Doa.objects.all()
        data = []
        for d in doa:
            data.append({
                'id': d.id,
                'doa_name': d.doa_name,
                'doa_full_text_translate': d.doa_full_text_translate,
                'quri_name': d.quri_name,
                'doa_category': d.doa_category,
                'doa_sound': f'{request.scheme}://{request.get_host()}/media/' + str(d.doa_sound),
                'date_created': d.date_created,
            })
        return JsonResponse(data, safe=False)


def ahadis(request):
    count = Ahadis.objects.count()
    if count == 0:
        return JsonResponse({'error': []})
    else:
        ahadis = Ahadis.objects.all()
        data = []
        for a in ahadis:
            data.append({
                'id': a.id,
                'ahadis_title': a.ahadis_title,
                'ahadis_text_ar': a.ahadis_text_ar,
                'ahadis_text_translate': a.ahadis_text_translate,
                'ahadis_source': a.ahadis_source,
                'date_created': a.date_created,
            })
        return JsonResponse(data, safe=False)


def ziyart_majazi(request):
    count = ZiyartMajazi.objects.count()
    if count == 0:
        return JsonResponse({'error': []})
    else:
        ziyart_majazi = ZiyartMajazi.objects.all()
        data = []
        for z in ziyart_majazi:
            data.append({
                'id': z.id,
                'ziyart_majazi_title': z.ziyart_majazi_title,
                'ziyart_majazi_img': f'{request.scheme}://{request.get_host()}/media/' + str(z.ziyart_majazi_img),
                'ziyart_majazi_link': z.ziyart_majazi_link,
                'date_created': z.date_created,
            })
        return JsonResponse(data, safe=False)


def vasiatnameh_shohada(request):
    count = VasiatnamehShohada.objects.count()
    if count == 0:
        return JsonResponse({'error': []})
    else:
        vasiatnameh_shohada = VasiatnamehShohada.objects.all()
        data = []
        for v in vasiatnameh_shohada:
            data.append({
                'id': v.id,
                'vasiatnameh_shohada_name': v.vasiatnameh_shohada_name,
                'vasiatnameh_shohada_img': f'{request.scheme}://{request.get_host()}/media/' + str(v.vasiatnameh_shohada_img),
                'vasiatnameh_shohada_text': v.vasiatnameh_shohada_text,
                'date_created': v.date_created,
            })
        return JsonResponse(data, safe=False)
