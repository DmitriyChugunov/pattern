from django.contrib import admin
from django.urls import path, include

from .views import IndexView, AboutView, ContactsView, RegisterView

urlpatterns = [
    path('', IndexView, name='index'),
    path('about', AboutView, name='about'),
    path('contacts', ContactsView, name='contacts'),
    path('form', RegisterView, name='form')
]