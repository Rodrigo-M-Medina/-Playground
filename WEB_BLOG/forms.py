from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm



class EditarUsuario(UserCreationForm):
    username=forms.CharField(label="Ingrese Usuario")
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio 


