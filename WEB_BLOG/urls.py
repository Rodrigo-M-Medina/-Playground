from django.urls import path
from WEB_BLOG.views import blog, edicionUsuario, fotoPerfil, Titulos, mostrar
from WEB_LR.views import salir



urlpatterns = [
    path('blog1/', blog, name='blog'),
    path('salir/', salir, name="salir"),
    path("editarPerfil/", edicionUsuario, name='editarPerfil'),
    path("fotoPerfil/", fotoPerfil, name="fotoPerfil"),
    path("titulo/", Titulos, name="titulo"),
    path("buscar/", mostrar, name="mostrar"),
]