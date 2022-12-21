#import para autenticar, ingresar y desloguear usuario
from django.contrib.auth import login, authenticate, logout
#import para render
from django.shortcuts import render
#import de forms de WEB_LR
from WEB_LR.forms import RegistroUsuario, IngresoUsuario
#import de vistar de WEB_BLOG 
from WEB_BLOG.views import blog


#---------- pagina de inicio ----------------
def inicio(request):
    return render(request, "pagina_inicio.html")


#---------- pagina de registro ----------------
def registro(request):
    if request.method=="POST":
        form=RegistroUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")# ver porque queda de ese color user name!!!
            form.save()

            return render(request, "pagina_inicio.html")
        else:
            return render(request, "registro.html", {"form":form, "mensaje":"Error al crear el usuario"})
    
    else:
        form=RegistroUsuario()
    return render(request, "registro.html", {"form":form})


#---------- pagina de ingreso ----------------
def ingreso(request):
    if request.method == "POST":
        form=IngresoUsuario(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:    
                login(request, usuario)
                return blog(request, usuario)
            else:
                return render(request, 'ingreso.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            return render(request, 'ingreso.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = IngresoUsuario()
    return render(request, 'ingreso.html', {"form":form})


#---------- funcion desconectarse ----------------

def salir(request):
    logout(request)
    return render(request, "pagina_inicio.html")
