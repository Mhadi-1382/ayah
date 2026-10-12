from django.shortcuts import redirect
from .models import Notes, Bookmarks

def notes(request):
    if request.user.is_authenticated:
        note = Notes.objects.filter(user=request.user)
        notes_data = [{
            'id': note.id,
            'user': note.user.id,
            'title': note.title_note,
            'text': note.text_note,
            'date_created': note.date_created
            } for note in note]

        return {'notes': notes_data}
    else:
        note = []
        return {'notes': note}


def bookmarks(request):
    if request.user.is_authenticated:
        bookmark = Bookmarks.objects.filter(user=request.user)
        bookmarks_data = [{
            'id': bookmark.id,
            'user': bookmark.user.id,
            'title_bookmark': bookmark.title_bookmark,
            'link_bookmark': bookmark.link_bookmark,
            'date_created': bookmark.date_created
            } for bookmark in bookmark]

        return {'bookmarks': bookmarks_data}
    else:
        bookmark = []
        return {'bookmarks': bookmark}

def bookmarks_check_content(request):
    if request.user.is_authenticated:
        bookmark = Bookmarks.objects.filter(user=request.user).values_list('link_bookmark', flat=True)
        return {'bookmarks_check_content': ','.join(bookmark)}
    else:
        bookmark = []
        return {'bookmarks_check_content': bookmark}
