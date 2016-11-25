from django.shortcuts import render

from models import Poster


def index(request):
    posters = Poster.objects.all()
    return render(request, 'index.html')
