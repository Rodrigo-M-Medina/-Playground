from django.urls import path, include
from WEB_BLOG.views import blog, edicionUsuario, fotoPerfil, buscar, crearPost
from WEB_LR.views import salir



urlpatterns = [
    path('blog1/', blog, name='blog'),
    path('salir/', salir, name="salir"),
    path("editarPerfil/", edicionUsuario, name='editarPerfil'),
    path("fotoPerfil/", fotoPerfil, name="fotoPerfil"),
    path("buscar/", buscar, name="buscar"),
    path("crear/", crearPost, name="crear"),
]