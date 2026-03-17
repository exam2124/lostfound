# core/urls.py
# This file maps URLs to their view functions

from django.urls import path
from . import views

urlpatterns = [
    # Root URL → redirect to login
    path('',        views.login_view,  name='login_redirect'),

    # Auth pages
    path('signup/', views.signup_view, name='signup'),
    path('login/',  views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Main app pages
    path('home/',   views.home_view,   name='home'),
    path('items/',  views.items_view,  name='items'),
]