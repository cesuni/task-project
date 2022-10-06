from django.shortcuts import render

# Create your views here.


def bitacora(request):
    return render(request, 'bitacora.html')
