from django.http import HttpResponse
from django.template import Template, Context, loader

def saludar(request):
    return HttpResponse("Hola Mundo!")

def segunda_vista(request):
    return HttpResponse("Ahora siiiii (?)")

def probandoHTML(request):

    dicc={"nombre":"Leandro", "vinculo":"Hijo", "edad": 27, "fechanac": "1995-06-27"}

    template=loader.get_template("template.html")

    documento=template.render(dicc)
    return HttpResponse(documento)