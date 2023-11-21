from django.urls import path
from .views import home, signup, thanks, signin, post_list, signout

urlpatterns = [
    path('', home, name='home'),
    path('thanks/', thanks, name='thanks'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('posts/', post_list, name='post_list'),
    path('signout/', signout, name='signout'),
]
