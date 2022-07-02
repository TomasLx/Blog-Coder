from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from blogcoder.forms import UserRegistrationForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blogcoder.models import Blogs
from django.urls import reverse_lazy;
from django.contrib.auth.decorators import login_required

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

class BlogDetalle(DetailView):

    model = Blogs
    template_name= "blogcoder/blog_detail.html"



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


class BlogCreacion(CreateView):

    model = Blogs
    success_url = "/blogcoder/blog"
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "imagen", "fecha" ]
class BlogUpdate(UpdateView):

    model = Blogs
    success_url = "/blogcoder/blog"
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "imagen", "fecha" ]
class BlogDelete(DeleteView):
    model = Blogs
    success_url = "/blogcoder/blog"

@login_required
def editarPerfil(request):
  usuario = request.user

  if request.method == 'POST':
    formulario = UserEditForm(request.POST, instance=usuario)
    if formulario.is_valid():
      informacion = formulario.cleaned_data
      usuario.email = informacion['email']
      usuario.password1 = informacion['password1']
      usuario.password2 = informacion['password2']
      usuario.save()

      return render(request, 'blogcoder/inicio.html', {'usuario': usuario, 'mensaje': 'Datos actualizados correctamente'})
  else:
    formulario = UserEditForm(instance=usuario)
  return render(request, 'blogcoder/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username})