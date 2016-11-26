from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Poster, Reaction, Comment
from .utils import paginate
from .forms import AddReactionForm, AttachCommentForm, VoteCommentForm


def index(request):
    posters = [
        {
            'text'     : poster.text,
            'slug'     : poster.slug,
            'reactions': poster.reaction_counts()
        }
        for poster in Poster.objects.all()
    ]

    return render(request, 'index.html', { 'posters': posters })

def feed(request):
    return render(request, 'feed.html')


def poster_view(request, slug, comment_id=None, page=None):
    poster = get_object_or_404(Poster, slug=slug)

    # Fetch total reaction counts:
    reactions = poster.reaction_counts()

    # Fetch page of comments:
    start, end = paginate(page)

    comments = list(Comment.objects
        .filter(reaction__poster=poster)
        .exclude(id=comment_id)
        .order_by('-votes')
        [start:end]
    )

    # If given a specific comment, place it first:
    if comment_id:
        comments.insert(0, get_object_or_404(Comment, id=comment_id))

    my_reaction = Reaction.objects.filter(poster=poster, author=request.user).first()

    return render(request, 'poster.html', {
        'poster'     : poster,
        'reactions'  : reactions,
        'comments'   : comments,
        'my_reaction': my_reaction
    })


def add_reaction(request):
    form = AddReactionForm(request.POST)

    if form.is_valid():
        data = form.clean()
        data['poster'].react(request.user, data['type'])

        return HttpResponse()

    else:
        print form.errors
        return HttpResponseBadRequest()

def attach_comment(request):
    form = AttachCommentForm(request.POST)

    if form.is_valid():
        data = form.clean()
        reaction = data['reaction']

        try:
            reaction.set_comment(data['text'])
            return redirect('poster_view_comment', slug=reaction.poster.slug, comment_id=reaction.comment.id)

        except Exception as e:
            print e
            return redirect('poster_view', slug=reaction.poster.slug)

    else:
        print form.errors


def vote_comment(request):
    form = VoteCommentForm(request.POST)

    if form.is_valid():
        data = form.clean()
        data['comment'].vote(request.user)

        return HttpResponse()

    else:
        print form.errors
        return HttpResponseBadRequest()
