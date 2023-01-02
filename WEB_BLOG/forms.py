from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from WEB_BLOG.models import *

#---------------form de mensajes------------------

class MensajeForm(forms.ModelForm):#solo necesito traer por meta el model Chat y sus field 
    class Meta:
        model = Chat
        fields = ['entrada', 'mensaje']

#----------------form para editar el usuario --------------------------------

class EditarUsuario(UserCreationForm):
    username=forms.CharField(label="Ingrese Usuario")
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio 

#---------- form para cargar imagenes al perfil --------------------------

class ImagenPerfilForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

#--------------------- post para crear posteos desde ------------

class PosteoForm(forms.Form):
    titulo=forms.CharField(label="ingrese el titulo")
    imagen=forms.ImageField(label="Imagen")
    descripcion=forms.CharField(label="descripcion")


