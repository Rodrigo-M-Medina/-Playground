from django.shortcuts import render


# Create your views here.
def blog(request, usuario):
    return render(request, "blog.html", {'mensaje':f"Bienvenido {usuario}" })
