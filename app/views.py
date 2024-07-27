from django.shortcuts import render
from .models import Index



def index(request):

    context = {
    'index': Index.objects.all()
    }
    return render(request, 'index.html', context)
