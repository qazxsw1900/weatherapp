from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name='notes/notes'),
    path('new/', views.new, name='notes/notes'),
    path('<int:note_id>', views.delete, name='notes/notes'),
]