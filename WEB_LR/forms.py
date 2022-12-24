from django import forms
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



# ----------------- Form de registro ---------------------------
class RegistroUsuario(UserCreationForm):
    #form para crear un usuario propio desde la pagina y RegexValidator para validar que el usuario use esos caracteres 
    username=forms.CharField(label="Ingrese Usuario", validators=[
            RegexValidator(r'^[\w.@+-]+$','Introduzca un nombre de usuario válido. Este valor puede contener solo letras, números y caracteres @/./+/-/_.','invalido')])
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio

# ----------------- Form de iniciar sesion ---------------------------

class IngresoUsuario(AuthenticationForm):
    username = forms.CharField(label="Ingrese Usuario")
    password = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
