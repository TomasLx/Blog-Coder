from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from ckeditor.fields import RichTextField

class Blogs(models.Model):

    titulo = models.CharField(max_length=50)

    subtitulo = models.CharField(max_length=50)

    cuerpo = RichTextField()

    autor = models.CharField(max_length=255)

    imagen = models.CharField(max_length=2555)

    fecha = models.DateTimeField()

    def __str__(self):
        return f"Titulo y Autor: {self.titulo}, {self.autor}"