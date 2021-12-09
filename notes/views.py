from django.shortcuts import render
from .models import Notes

# Create your views here.


def notes_view(request):
    if request.method == 'POST':
        current_user = request.user
        new_note = Notes(user=current_user)
        new_note.save()
    notes = Notes.objects.all()
    return render(request, 'notes/notes.html', {'notes': notes})