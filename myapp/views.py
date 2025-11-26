#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def acceuil(request):
    return render(request, 'acceuil.html')

def formation(request):
    return render(request, 'formation.html')
    
def experience(request):
    return render(request, 'experience.html')

def projet(request):
    return render(request, 'projet.html')

def contact(request):
    return render(request, 'contact.html')


