from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import Poster, Comment
# from .forms import AddCommentForm
from .utils import paginate


def index(request):
    return render(request, 'index.html', {
        'posters': Poster.objects.all()
    })


def comments_view(request, slug, comment_id=None, page='1'):
    poster = get_object_or_404(Poster, slug=slug)

    start, end = paginate(page)

    # Fetch the comments in range:
    comments = list(poster.comments.exclude(id=comment_id)[start:end])

    # If given a specific comment, place it first:
    if comment_id:
        comments.insert(0, get_object_or_404(Comment, id=comment_id))

    return render(request, 'comments.html', {
        'poster'  : poster,
        'comments': comments
    })


def comments_add(request, slug):
    poster = get_object_or_404(Poster, slug=slug)

    form = AddCommentForm(request.POST)

    if form.is_valid():
        props = form.validated_data
        comment = Comment.objects.create(**props)

        return redirect('comments_view', slug=poster.slug, comment_id=comment.id)

    else:
        return HttpResponseBadRequest()
