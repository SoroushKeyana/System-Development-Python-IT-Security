from django.urls import path
from .views import user_list, index, user_form

urlpatterns = [
    path('', index, name = 'index'),
    path('users/', user_list, name='user_list'),
    path('user-form', user_form, name= 'user_form')
]