from __future__ import unicode_literals

from django.forms import *
from .models import Poster, Reaction, Comment


class AddReactionForm(Form):
    poster = ModelChoiceField(queryset=Poster.objects.all())
    type   = CharField(max_length=10)


class AttachCommentForm(Form):
    reaction = ModelChoiceField(queryset=Reaction.objects.all())
    text     = CharField(max_length=5000, required=False)


class VoteCommentForm(Form):
    comment = ModelChoiceField(queryset=Comment.objects.all())
