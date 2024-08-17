from django.shortcuts import render
from.models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django .shortcuts import get_object_or_404
import datetime

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})

def registross(request):

    return render(request, "registros/principal.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()#inserta
            return render(request,'registros/contacto.html')
    form = ComentarioContactoForm()

    return render(request,'registros/contacto.html',{'form':form})

def contacto(resquet):
   return render(resquet,"registros/contacto.html")

def consultarComentarios(request):
    comentarios_contactos = ComentarioContacto.objects.all()
    return render(request, "registros/consultarComentario.html", {'ComentariosContactos': comentarios_contactos})

def eliminarComentarioContactoo(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios_contactos = ComentarioContacto.objects.all()
        return render(request, "registros/consultarComentario.html", {'ComentariosContactos': comentarios_contactos})
    return render(request, confirmacion, {'object': comentario})


def consultarComentarioIndividual(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    return render(request, "registros/formEditComentario.html", {'comentario': comentario})

def editarComentarioContactoo(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultarComentario.html", {'ComentariosContactos': comentarios})
    else:
        form = ComentarioContactoForm(instance=comentario)
    return render(request, "registros/formEditComentario.html", {'form': form, 'comentario': comentario})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="matutino")
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2024, 7, 17)
    fechaFin = datetime.date(2024, 7, 17)
    alumnos=Alumnos.objects.filter(created__range= (fechaInicio, fechaFin))
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request, "registros/consultas.html",{'alumnos':alumnos})