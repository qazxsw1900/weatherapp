from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name='notes/notes'),
    path('new/', views.new, name='notes/new'),
    path('delete/<int:note_id>', views.delete, name='notes/delete'),
    path('edit/<int:note_id>', views.edit, name='notes/edit'),
]