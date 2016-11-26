from django.shortcuts import render

from .models import Poster
# from .forms import AddCommentForm


def index(request):
    return render(request, 'index.html', {
        'posters': Poster.objects.all()
    })




# def add_comment(request):
#     form = AddCommentForm(request.POST)

#     if form.is_valid():
#         return asd

#     else:
#         return other
