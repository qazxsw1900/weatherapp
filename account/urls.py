from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='login'),
    path('login/', views.log_in, name='register'),
    path('logout/', views.log_out, name='register')
]