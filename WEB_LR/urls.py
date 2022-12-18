from django.urls import path
from WEB_LR.views import *

urlpatterns = [
    path('ingreso/', ingreso, name="ingreso"),
    path('registro/', registro, name="registro"),
    path('desconectarse/', desconectarse, name="desconectarse"),
    path('blog/', blog, name="blog"),
    path('', inicio, name="inicio"),
]