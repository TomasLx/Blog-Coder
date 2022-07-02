from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from blogcoder.forms import UserRegistrationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blogcoder.models import Blogs


def inicio(request):
    plantilla = loader.get_template('blogcoder/Inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def blog(request):
    blogs = Blogs.objects.all()
    contexto = { 'blogs' : blogs}
    plantilla = loader.get_template('blogcoder/blog.html')
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

class BlogCreacion(CreateView):

    model = Blogs
    success_url = "/blogcoder/blog"
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "imagen", "fecha" ]
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, 'blogcoder/Inicio.html', {'mensaje':f'Bienvenido{usuario}'})
            else:
                return render(request, 'blogcoder/Inicio.html', {'mensaje':'Error, datos incorrectos'})
        else:
            return render(request, 'blogcoder/Inicio.html', {'mensaje':'Error, formulario erroneo'})
    form = AuthenticationForm()
    return render(request, 'blogcoder/login.html',{'form':form})

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'blogcoder/Inicio.html' , {'mensaje':'Usuario Creado'})
    else:
        form = UserRegistrationForm()
    return render(request, 'blogcoder/registro.html', {'form': form})

