from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import Poster, Reaction, Comment
from .utils import paginate
from .forms import AddReactionForm, AttachCommentForm


def index(request):
    return render(request, 'index.html', {
        'posters': Poster.objects.all()
    })


def poster_view(request, slug, comment_id=None, page=None):
    poster = get_object_or_404(Poster, slug=slug)

    # Fetch total reaction counts:
    reactions = {
        'ouch' : Reaction.objects.filter(poster=poster, type=Reaction.Type.OUCH).count(),
        'sorry': Reaction.objects.filter(poster=poster, type=Reaction.Type.SORRY).count()
    }

    # Fetch page of comments:
    start, end = paginate(page)

    comments = list(Comment.objects
        .filter(reaction__poster=poster)
        .exclude(id=comment_id)
        [start:end]
    )

    # If given a specific comment, place it first:
    if comment_id:
        comments.insert(0, get_object_or_404(Comment, id=comment_id))

    return render(request, 'poster.html', {
        'poster'   : poster,
        'reactions': reactions,
        'comments' : comments
    })


def add_reaction(request):
    form = AddReactionForm(request.POST)

    if form.is_valid():
        data = form.clean()

        try:
            data['poster'].react(request.user, data['type'])
        except:
            pass

        return redirect('poster_view', slug=data['poster'].slug)


# def attach_comment
