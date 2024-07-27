from django.shortcuts import render
from .models import Index



def index(request):
    context = {

    }
    return render(request, 'index.html', context)
