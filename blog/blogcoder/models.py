from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

class Blogs(LoginRequiredMixin):

    titulo = models.CharField(max_length=50)

    subtitulo = models.CharField(max_length=50)

    cuerpo = models.CharField(max_length=255)

    autor = models.CharField()

    imagen = models.CharField()

    fecha = models.DateTimeField()

    def __str__(self):
        return f"Titulo y Autor: {self.titulo}, {self.autor}"