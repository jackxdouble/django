from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse('hola')
    
def segunda_vista(request):
    return HttpResponse('esta es la segunda vista')

def diahoy(request):
    dia = datetime.datetime.now()

    texto = f'ho dia es {dia}'

    return HttpResponse(texto)