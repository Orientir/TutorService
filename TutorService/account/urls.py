from django.urls import path
from django.contrib.auth import views as django_views

from . import views

urlpatterns = [
    path('', views.details, name="details"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('password/reset/', views.password_reset, name="reset-password"),
]