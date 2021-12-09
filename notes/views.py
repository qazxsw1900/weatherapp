from django.shortcuts import render, redirect
from .models import Notes


# Create your views here.


def notes_view(request):
    current_user = request.user
    notes = Notes.objects.filter(user=current_user)
    return render(request, 'notes/notes.html', {'notes': notes})


def new(request):
    current_user = request.user
    if request.method == 'POST':
        title = request.POST['title']
        detail = request.POST['detail']
        new_note = Notes(user=current_user, note_header=title, note_content=detail)
        new_note.save()
        response = redirect('/notes')
        return response
    return render(request, 'notes/new.html', {'notes': None})


def delete(request, note_id):
    Notes.objects.filter(id=note_id).delete()
    response = redirect('/notes')
    return response
