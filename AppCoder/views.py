from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def peliculas(request):
    return render (request, "AppCoder/listarPelis.html")

def directores(request):
    return render (request, "AppCoder/directores.html")

def actores(request):
    return render (request, "AppCoder/actores.html")

def inicio(request):
    return render (request, "AppCoder/inicio.html")

@login_required
def mostrarAvatar(request):
    lista = Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
            avatar = lista[0].imagen.url
    else:
            avatar = "media/avatars/default.png"
    return avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        formu = AvatarForm(request.POST, request.FILES)
        if formu.is_valid():
            avatar = Avatar(user=request.user, imagen=request.FILES['imagen'])
            avatarAnterior = Avatar.objects.filter(user=request.user)
            if len(avatarAnterior)>0:
                avatarAnterior.delete()
            avatar.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Avatar guardado con éxito"})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form": formu, "usuario": request.user, "mensaje": "Error al guardar el avatar"})
    else:
        form = AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user})
    

#Forms para cargar

@login_required
def peliFormulario(request):
    if request.method == "POST":
        form = PeliForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            anio = detalles["anio"]
            duracion = detalles["duracion"]
            pais = detalles["pais"]
            director = detalles["director"]
            poster = detalles["poster"]

            nuevaPeli = pelicula(nombre=nombre, anio=anio, duracion=duracion, pais=pais, director=director, poster=poster)
            nuevaPeli.save()
            return render(request, "AppCoder/listarPelis.html", {"mensaje": "Película guardada con éxito"})

        else:
            return render(request, "AppCoder/peliFormulario.html", {"form": form, "mensaje": "Error al guardar la película"})
    else:
        formulario = PeliForm()
        return render(request, "AppCoder/peliFormulario.html", {"form": formulario})

@login_required
def actorForm(request):
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            apellido = detalles["apellido"]
            edad = detalles["edad"]
            nacionalidad = detalles["nacionalidad"]
            foto = detalles["foto"]

            nuevoActor = actor(nombre=nombre, apellido=apellido, edad=edad, nacionalidad=nacionalidad, foto = foto)
            nuevoActor.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Actor guardado con éxito"})

        else:
            return render(request, "AppCoder/actorForm.html", {"form": formulario, "mensaje": "Error al guardar el actor"})

    else:
        formulario = ActorForm()
        return render(request, "AppCoder/actorForm.html", {"form": formulario})

@login_required
def directorForm(request):
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            apellido = detalles["apellido"]
            edad = detalles["edad"]
            nacionalidad = detalles["nacionalidad"]
            foto = detalles["foto"]

            nuevoDirector = director(nombre=nombre, apellido=apellido, edad=edad, nacionalidad=nacionalidad, foto = foto)
            nuevoDirector.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Director guardado con éxito"})

        else:
            return render(request, "AppCoder/directorForm.html", {"form": formulario, "mensaje": "Error al guardar el director"})

    else:
        formulario = DirectorForm()
        return render(request, "AppCoder/directorForm.html", {"form": formulario})

# Funciones y clases de pelis

def busquedaPeli(request):
    return render (request, "AppCoder/busquedaPeli.html")

def buscarPeli(request):
    nombre = request.GET["nombre"]
    if nombre !="":
        pelis = pelicula.objects.filter(nombre__icontains=nombre)
        return render (request, "AppCoder/resBusqPelis.html", {"pelis": pelis})
    else:
        return render (request, "AppCoder/busquedaPeli.html", {"mensaje": "No se encontró la película"})

def listarPelis(request):
    pelis = pelicula.objects.all()
    return render (request, "AppCoder/listarPelis.html", {"pelis": pelis})

@login_required
def editarPeli(request, id):
    peli = pelicula.objects.get(id=id)
    if request.method == "POST":
        form = PeliForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            peli.nombre = detalles["nombre"]
            peli.anio = detalles["anio"]
            peli.duracion = detalles["duracion"]
            peli.pais = detalles["pais"]
            peli.director = detalles["director"]
            peli.poster = detalles["poster"]
            peli.save()
            pelis = pelicula.objects.all()
            return render(request, "AppCoder/listarPelis.html", {"pelis": pelis, "mensaje": "Película editada con éxito"})
        pass
    else:
        formulario = PeliForm(initial = {"nombre": peli.nombre, "anio": peli.anio, "duracion": peli.duracion, "pais": peli.pais, "director": peli.director, "poster": peli.poster})
        return render(request, "AppCoder/editarPeli.html", {"form": formulario, "peli": peli})

class borrarPeli(DeleteView, LoginRequiredMixin):
    model = pelicula
    success_url = reverse_lazy("listarPelis")

# Funciones y clases de directores

def busquedaDirector(request):
    return render (request, "AppCoder/busquedaDirector.html")

def buscarDirector(request):
    nombre = request.GET["nombre"]
    if nombre !="":
        directores = director.objects.filter(nombre__icontains=nombre)
        return render (request, "AppCoder/resBusqDirectores.html", {"directores": directores})
    else:
        return render (request, "AppCoder/busquedaDirector.html", {"mensaje": "No se encontró al director"})

def listarDirectores(request):
    directores = director.objects.all()
    return render (request, "AppCoder/listarDirectores.html", {"directores": directores})

@login_required
def editarDirector(request, id):
    directors = director.objects.get(id=id)
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            directors.nombre = detalles["nombre"]
            directors.apellido = detalles["apellido"]
            directors.edad = detalles["edad"]
            directors.nacionalidad = detalles["nacionalidad"]
            directors.foto = detalles["foto"]
            directors.save()
            directores = director.objects.all()
            return render(request, "AppCoder/listarDirectores.html", {"directores": directores, "mensaje": "Director editado con éxito"})
        pass
    else:
        formulario = DirectorForm(initial = {"nombre": directors.nombre, "apellido": directors.apellido, "edad": directors.edad, "nacionalidad": directors.nacionalidad, "foto": directors.foto})
        return render(request, "AppCoder/editarDirector.html", {"form": formulario, "director": directors})

class borrarDirector(DeleteView, LoginRequiredMixin):
    model = director
    success_url = reverse_lazy("listarDirectores")

# Funciones y clases de actores

def busquedaActor(request):
    return render (request, "AppCoder/busquedaActor.html")

def buscarActor(request):
    nombre = request.GET["nombre"]
    if nombre !="":
        actores = actor.objects.filter(nombre__icontains=nombre)
        return render (request, "AppCoder/resBusqActores.html", {"actores": actores})
    else:
        return render (request, "AppCoder/busquedaActor.html", {"mensaje": "No se encontró al actor"})

def listarActores(request):
    actores = actor.objects.all()
    return render (request, "AppCoder/listarActores.html", {"actores": actores})

@login_required
def editarActor(request, id):
    actors = actor.objects.get(id=id)
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            actors.nombre = detalles["nombre"]
            actors.apellido = detalles["apellido"]
            actors.edad = detalles["edad"]
            actors.nacionalidad = detalles["nacionalidad"]
            actors.foto = detalles["foto"]
            actors.save()
            actores = actor.objects.all()
            return render(request, "AppCoder/listarActores.html", {"actores": actores, "mensaje": "Actor editado con éxito"})
        pass
    else:
        formulario = ActorForm(initial = {"nombre": actors.nombre, "apellido": actors.apellido, "edad": actors.edad, "nacionalidad": actors.nacionalidad, "foto": actors.foto})
        return render(request, "AppCoder/editarActor.html", {"form": formulario, "actor": actors})

class borrarActor(DeleteView, LoginRequiredMixin):
    model = actor
    success_url = reverse_lazy("listarActores")

# Vista de registro

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
           username = form.cleaned_data["username"]
           form.save()
           return render(request, "AppCoder/inicio.html", {"mensaje": f"Registro del usuario {username} exitoso"})
        else:
            return render(request, "AppCoder/registroForm.html", {"form": form})
    else:
        form = RegistroUsuarioForm()
        return render(request, "AppCoder/registroForm.html", {"form": form})

# Vista de login

def ingreso(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            user=datos["username"]
            contrasenia=datos["password"]
            usuario = authenticate(username=user, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Ingreso del usuario {user} exitoso"})
            else:
                return render(request, "AppCoder/loginForm.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/loginForm.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "AppCoder/loginForm.html", {"form": form})
    
        


# Editar perfiles

@login_required
def EditarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = EditarPerfilForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario.email = datos["email"]
            usuario.password1 = datos["password1"]
            usuario.password2 = datos["password2"]
            usuario.first_name = datos["first_name"]
            usuario.last_name = datos["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Perfil editado con éxito"})
        else:
            return render(request, "AppCoder/editarPerfil.html", {"form": form})
    else:
        form = EditarPerfilForm(instance=usuario)
        return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario": usuario.username})

# Carga posters de películas
