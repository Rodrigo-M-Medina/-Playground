from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#----------- chat ------------------

class Chat(models.Model):
    salida = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salida') #related_name en teoria me deja darle un field
    entrada = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entrada')
    mensaje = models.TextField()
    tiempo = models.DateTimeField(auto_now_add=True)

#------------- cargar imagen de perfil ----------------
class ImagenPerfil(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
#-------------------- cargar posteo -------------------------
class Posteo(models.Model):
    titulo=models.CharField(max_length=20)
    descripcion=RichTextField(blank=True,null=True)
    imagen=models.ImageField(upload_to='posteos')
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.usuario} - {self.imagen} - {self.titulo} - {self.descripcion}" 