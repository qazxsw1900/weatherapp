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
    return render(request, 'notes/new.html', {'note': None, 'title': 'New Note', 'submit': 'Create'})


def edit(request, note_id):
    current_user = request.user
    try:
        note = Notes.objects.get(user=current_user, pk=note_id)
    except:
        response = redirect('/notes')
        return response
    if request.method == 'POST':
        note.note_header = request.POST['title']
        note.note_content = request.POST['detail']
        note.save()
        response = redirect('/notes')
        return response
    return render(request, 'notes/new.html', {'note': note, 'title': 'Edit Note', 'submit': 'Save'})


def delete(request, note_id):
    current_user = request.user
    try:
        Notes.objects.filter(user=current_user, id=note_id).delete()
    except:
        pass
    response = redirect('/notes')
    return response
