from django.urls import path
from .views import index, help

urlpatterns = [
    path('', index, name='hello_world'),
    path('help/', help, name='help'),
]
