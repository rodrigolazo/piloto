# Create your views here.
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from aplicacion1.models import Persona
from aplicacion1.formularios import FormularioPersonas
from django.shortcuts import render
from django.http import HttpResponseRedirect

def mostrarTexto(request):
    return render_to_response("mipagina.html")

def mostrarTabla(request):
    personas = Persona.objects.all()
    return render_to_response('tabla.html',{'personas': personas })

def formulario(request):
    if request.method=="POST":
        formulario=FormularioPersonas(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/tabla")
    else:
        formulario=FormularioPersonas()
    return render(request, 'agregarPersona.html', {'formulario': formulario})
    #-------------
def eliminar_persona(request, id_persona):
    persona=Persona.objects.get(id=id_persona)
    persona.delete()
    return HttpResponseRedirect("/tabla")    

def editar_persona(request, id_persona):
    persona=Persona.objects.get(id=id_persona)
    if request.method=="POST":
        formulario=FormularioPersonas(request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/tabla")
    else:
        formulario = FormularioPersonas(instance=persona)
    return render_to_response("editar.html",{"formulario":formulario},context_instance=RequestContext(request))

