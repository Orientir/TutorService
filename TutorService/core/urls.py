from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('404', views.handle_404, name="handle-404"),
]