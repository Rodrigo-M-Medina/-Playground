from django.db import models
from django.contrib.auth.models import User


class ImagenPerfil(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Posteo(models.Model):
    titulo=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=800)
    imagen=models.ImageField(upload_to='posteos')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen} - {self.titulo} - {self.descripcion}" 