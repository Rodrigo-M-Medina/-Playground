from django.shortcuts import render
from WEB_BLOG.forms import EditarUsuario, ImagenPerfilForm
from WEB_BLOG.models import ImagenPerfil, Posteo



#------- pagina a la que se ingresa por medio del login de WEB_LR --------
def blog(request, usuario):
    return render (request, "blog.html", {"mensaje": f"bienvenido{usuario}", "imagen":mostrarImagen(request)})



#------------- Buscar Posteos -------------------

def Titulos(request):
    return render(request, "busqueda.html.html")

def mostrar(request):
    var1=Posteo.objects.all()
    return render(request,"resultados.html", {"resultado":var1})


'''def buscar(request):
    if "titulo" in (request.GET):
        var1=request.GET ["titulo"]
        resultado=Posteo.objects.filter(titulo__icontains=var1)
        imagen=mostrarPost("titulo")
        return render(request,"resultados.html", {"resultado":resultado}, {"imagen":imagen})
    else:
        return render(request, "busqueda.html", {"mensaje":"no se encontro el post"})'''



#-------  FUNCION PARA AGREGAR IMAGEN ---------

def fotoPerfil(request):
    if request.method=="POST":
        form=ImagenPerfilForm(request.POST, request.FILES)
        if form.is_valid():
            imagenXdefecto=ImagenPerfil.objects.filter(user=request.user)
            if len(imagenXdefecto)!=0:
                imagenXdefecto[0].delete()
            imagen=ImagenPerfil(user=request.user, imagen=request.FILES["imagen"])
            imagen.save()
            return render(request, "blog.html", {"imagen":mostrarImagen(request)})
        else:
            return render(request, "agregarImagen.html", {"formulario": form, "usuario": request.user})
    else:
        form=ImagenPerfilForm()
        return render(request , "agregarImagen.html", {"formulario": form, "usuario": request.user})

#--------- FUNCION PARA TRAER LA IMAGEN -----------------

def mostrarImagen(request):
    lista=ImagenPerfil.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.png"
    return imagen




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


