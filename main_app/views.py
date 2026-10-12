from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Notes, Bookmarks, Contactus
from panel_app.models import Surah, Doa, Ahadis, VasiatnamehShohada, ZiyartMajazi
from django.db.models import Count
import random

def index(request):
    count = Ahadis.objects.aggregate(count=Count('id'))['count']
    random_index = random.randint(0, count - 1) if count > 0 else None
    hadis_ruz = Ahadis.objects.all()[random_index] if random_index is not None else None
    return render(request, 'index.html', {'hadisRuz': hadis_ruz})


def search(request):
    query = request.GET.get('q', '')
    if query:
        surahs = Surah.objects.filter(surah_name_fa__icontains=query).values('id', 'surah_name_fa')
        doas = Doa.objects.filter(doa_name__icontains=query).values('id', 'doa_name')
        ahadis = Ahadis.objects.filter(ahadis_title__icontains=query).values('id', 'ahadis_title')
        ziyart_majazi = ZiyartMajazi.objects.filter(ziyart_majazi_title__icontains=query).values('id', 'ziyart_majazi_title', 'ziyart_majazi_link')
        vasiatnameh_shohada = VasiatnamehShohada.objects.filter(vasiatnameh_shohada_name__icontains=query).values('id', 'vasiatnameh_shohada_name')
    else:
        surahs, doas, ahadis, ziyart_majazi, vasiatnameh_shohada = [], [], [], [], []

    context = {
        'surah_search': surahs,
        'doa_search': doas,
        'ahadis_search': ahadis,
        'ziyart_majazi_search': ziyart_majazi,
        'vasiatnameh_shohada_search': vasiatnameh_shohada,
    }

    return render(request, 'includes/_search_results.html', context)


def contact_us(request):
    if request.method == 'POST':
        contactusUsername = request.POST.get('contactusUsername')
        contactusTel = request.POST.get('contactusTel')
        contactusEmail = request.POST.get('contactusEmail')
        contactusMessage = request.POST.get('contactusMessage')

        try:
            Contactus.objects.create(
                username = contactusUsername,
                phone = contactusTel,
                email = contactusEmail,
                message = contactusMessage
            )

            messages.success(request, 'نظر یا پیشنهاد شما با موفقیت ارسال شد.')
            return redirect(request.path)
        except Exception as e:
            messages.error(request, 'ارسال نظر یا پیشنهاد شما با مشکل مواجه شد. {0}'.format(e))
            return redirect(request.path)
    else:
        return redirect('/')


def surah(request):
    return render(request, 'pages/surah/surah.html', {'surah': Surah.objects.all()})

def surah_details(request, surah_id):
    slug_url = get_object_or_404(Surah, id=surah_id)
    if slug_url:
        return render(request, 'pages/surah/surah-details.html', {'surah': slug_url})


def doa(request):
    return render(request, 'pages/doa/doa.html', {'doa': Doa.objects.all()})

def doa_details(request, doa_id):
    slug_url = get_object_or_404(Doa, id=doa_id)
    if slug_url:
        return render(request, 'pages/doa/doa-details.html', {'doa': slug_url})

def doa_daily_prayers_ramadan(request):
        return render(request, 'pages/doa/doa-daily-prayers-ramadan.html')


def ahadis(request):
    return render(request, 'pages/ahadis/ahadis.html', {'ahadis': Ahadis.objects.all()})


def ziyart_majazi(request):
    return render(request, 'pages/ziyartMajazi/ziyartMajazi.html', {'ziyartMajazi': ZiyartMajazi.objects.all()})


def vasiatnameh_shohada(request):
    return render(request, 'pages/vasiatnamehShohada/vasiatnamehShohada.html', {'vasiatnamehShohada': VasiatnamehShohada.objects.all()})

def vasiatnameh_shohada_details(request, vasiatnameh_shohada_id):
    slug_url = get_object_or_404(VasiatnamehShohada, id=vasiatnameh_shohada_id)
    if slug_url:
        return render(request, 'pages/vasiatnamehShohada/vasiatnamehShohada-details.html', {'vasiatnamehShohada': slug_url})


def note_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            noteTitle = request.POST.get('noteTitle')
            noteText = request.POST.get('noteText')

            try:
                Notes.objects.create(
                    user = request.user,
                    title_note = noteTitle,
                    text_note = noteText
                )

                messages.success(request, 'یادداشت «{0}» با موفقیت ایجاد شد.'.format(noteTitle))
                return redirect(request.path)
            except Exception as e:
                messages.error(request, 'ایجاد یادداشت «{0}» با مشکل مواجه شد.'.format(noteTitle))
                return redirect(request.path)
        else:
            return redirect('/')
    else:
        return redirect('/')

def note_edit(request, note_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            noteForEditTitle = request.POST.get('noteForEditTitle')
            noteForEditText = request.POST.get('noteForEditText')

            note = get_object_or_404(Notes, id=note_id)
            try:
                note.title_note = noteForEditTitle
                note.text_note = noteForEditText
                note.save()

                messages.success(request, 'یادداشت «{0}» با موفقیت ویرایش شد.'.format(noteForEditTitle))
                return redirect(request.path)
            except Exception as e:
                messages.error(request, 'ویرایش یادداشت «{0}» با مشکل مواجه شد.'.format(noteForEditTitle))
                return redirect(request.path)
        else:
            return redirect('/')
    else:
        return redirect('/')

def note_remove(request, note_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            note = get_object_or_404(Notes, id=note_id)
            try:
                note.delete()

                messages.success(request, 'یادداشت با موفقیت حذف شد.')
                return redirect(request.path)
            except Exception as e:
                messages.error(request, 'حذف یادداشت با مشکل مواجه شد.')
                return redirect(request.path)
        else:
            return redirect('/')
    else:
        return redirect('/')


def bookmark_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bookmarkTitle = request.POST.get('bookmarkTitle')
            bookmarkLink = request.POST.get('bookmarkLink')

            try:
                Bookmarks.objects.create(
                    user = request.user,
                    title_bookmark = bookmarkTitle,
                    link_bookmark = bookmarkLink,
                )

                messages.success(request, 'محتوا «{0}» با موفقیت به لیست نشان شده ها اضافه شد.'.format(bookmarkTitle))
                return redirect(request.path)
            except Exception as e:
                messages.error(request, 'ثبت محتوا «{0}» با مشکل مواجه شد.'.format(bookmarkTitle))
                return redirect(request.path)
        else:
            return redirect('/')
    else:
        return redirect('/')

def bookmark_remove(request, bookmark_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bookmark = get_object_or_404(Bookmarks, id=bookmark_id)
            try:
                bookmark.delete()

                messages.success(request, 'محتوای نشان شده با موفقیت حذف شد.')
                return redirect(request.path)
            except Exception as e:
                messages.error(request, 'حذف محتوای نشان شده با مشکل مواجه شد.')
                return redirect(request.path)
        else:
            return redirect('/')
    else:
        return redirect('/')
