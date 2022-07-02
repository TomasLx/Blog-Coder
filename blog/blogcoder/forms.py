from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar e-mail")
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Modificar contraseña", widget=forms.PasswordInput)


    class Meta:

        model = User
        fields = ['email', 'password1', 'password2']