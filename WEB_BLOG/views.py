from django.shortcuts import render
from WEB_BLOG.forms import EditarUsuario





#------- pagina a la que se ingresa por medio del login de WEB_LR --------
def blog(request, usuario):
    return render (request, "blog.html", {"mensaje": f"bienvenido{usuario}"})

#-------  FUNCION PARA CARGAR  AVATAR ---------


#-------  EDICION DE DATOS DEL USUARIO LOGUEADO ---------

def edicionUsuario(request):
    usuario=request.user
    if request.method=="POST":
        form=EditarUsuario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.username=info["username"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "blog.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "mensaje":"Error al editar el perfil"})
    else:
        form=EditarUsuario(instance=usuario)
        return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username})


