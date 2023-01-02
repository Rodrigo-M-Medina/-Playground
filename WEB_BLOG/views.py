from django.shortcuts import render
from WEB_BLOG.forms import EditarUsuario, ImagenPerfilForm, PosteoForm, MensajeForm
from WEB_BLOG.models import ImagenPerfil, Posteo, Chat
from django.contrib.auth.models import User

#------------------ prueba de chat--------------------- por ahora funcional

def MandarMensajes(request):# por ahora solo puedo mandar mensajes desde un opcion de mensajes 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            # Guardando mensaje en la base de datos
            mensaje = form.save(commit=False)#commit false? se supone que es un booleano que me deja ver el mensaje antes de guardar
            mensaje.salida = request.user
            mensaje.save()
            mensajes = Chat.objects.all()  # obtengo todos los mensajes del modelo chat correjir
            return render(request, 'mandarMensajes.html', {'form': form, 'mensajes': mensajes})
    else:
        form = MensajeForm()
        mensajes = Chat.objects.all()  # obtengo todos los mensajes del modelo chat correjir
    return render(request, 'mandarMensajes.html', {'form': form, 'mensajes': mensajes})

#------- pagina a la que se ingresa por medio del login de WEB_LR --------
def blog(request):
    usuario=request.user
    return render (request, "blog.html", {"mensaje": f"bienvenido {usuario}", "imagen":mostrarImagen(request)})

#------------- Buscar Posteos Y Crear Posteos -------------------

def crearPost(request):
    if request.method=="POST":
        form=PosteoForm(request.POST, request.FILES)
        
        if form.is_valid():
            titulo=form.cleaned_data["titulo"]
            descripcion=form.cleaned_data["descripcion"]
            imagen=form.cleaned_data["imagen"]
            posteo=Posteo(titulo=titulo, descripcion=descripcion, imagen=imagen, usuario=request.user)
            posteo.save()
            return render(request, "blog.html")
    else:
        form=PosteoForm()
        return render(request, "agregarPosteo.html", {"form":form})


def buscar(request):
    if "titulo" in (request.GET):
        var1=request.GET ["titulo"]
        resultado=Posteo.objects.filter(titulo__icontains=var1)
        return render(request,"resultados.html", {"resultado":resultado})
    else:
        return render(request, "busqueda.html")


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


