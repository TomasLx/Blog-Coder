from django.contrib import admin
from django.urls import path, include
from .views import inicio, login_request, registro, blog, BlogCreacion, BlogDetalle, BlogDelete, BlogUpdate, editarPerfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path("", inicio, name="inicio" ),
    path("registro/", registro, name="registro"),
    path("logout/", LogoutView.as_view(template_name='blogcoder/logout.html'), name="logout"),
    path("blog/", blog, name="blog"),
    path("blogcreacion/", BlogCreacion.as_view(), name='New'),
    path("blogdetalle/<pk>", BlogDelete.as_view(), name='Delete'),
    path("blogupdate/<pk>", BlogUpdate.as_view(), name='Update'),
    path("blog/<pk>", BlogDetalle.as_view(), name='Detalle'),
    path("editarperfil/", editarPerfil, name='EditarPerfil'),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ]