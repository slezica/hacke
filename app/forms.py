from __future__ import unicode_literals

from django.forms import *
from .models import Poster, Comment


class AddCommentForm(Form):
    type   = CharField(max_length=10)
    text   = CharField(max_length=128)
    author = CharField(max_length=1024)

