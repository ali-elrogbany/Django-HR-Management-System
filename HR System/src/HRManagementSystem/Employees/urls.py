from django.contrib import admin
from django.urls import path

from .views import Create_view
from .views import Read_view
from .views import Update_view
from .views import Delete_view

urlpatterns = [
    path('create/', Create_view),
    path('', Read_view),
    path('update/<id>/', Update_view),
    path('delete/<id>/', Delete_view),
]
