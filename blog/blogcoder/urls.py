from django.contrib import admin
from django.urls import path, include
from .views import inicio, login_request, registro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path("", inicio, name="inicio" ),
    path("registro/", registro, name="registro"),
    path("logout/", LogoutView.as_view(template_name='blogcoder/logout.html'), name="logout"),
    ]