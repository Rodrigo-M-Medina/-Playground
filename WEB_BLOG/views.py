from django.shortcuts import render
from django.contrib.auth import logout


# Create your views here.
def blog(request, usuario):
    return render(request, "blog.html", {'mensaje':f"Bienvenido {usuario}" })

