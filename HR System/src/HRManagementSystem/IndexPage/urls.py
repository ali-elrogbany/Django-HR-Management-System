from django.contrib import admin
from django.urls import path

from .views import Index_view

urlpatterns = [
    path('', Index_view)
]
