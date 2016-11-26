from django.shortcuts import render

from .models import Poster, Comment
# from .forms import AddCommentForm
from .utils import paginate


def index(request):
    return render(request, 'index.html', {
        'posters': Poster.objects.all()
    })


def comments_view(request, slug, comment_id=None, page='1'):
    poster = Poster.objects.get(slug=slug)

    start, end = paginate(page)

    # Fetch the comments in range:
    comments = list(poster.comments.exclude(id=comment_id)[start:end])

    # If given a specific comment, place it first:
    if comment_id:
        comments.insert(0, Comment.objects.get(id=comment_id))

    return render(request, 'comments.html', {
        'poster'  : poster,
        'comments': comments
    })


def comments_add(request):
    pass
# def add_comment(request):
#     form = AddCommentForm(request.POST)

#     if form.is_valid():
#         return asd

#     else:
#         return other
