from django.shortcuts import render

from models import Poster


def index(request):
    return render(request, 'index.html', {
        'posters': Poster.objects.all()
    })
