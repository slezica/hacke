# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models import *


class Poster(Model):
    text = CharField(max_length=256)


class Comment(Model):
    class Type:
        OUCH  = 'ouch'
        SORRY = 'sorry'

    TYPE_CHOICES = [
        (Type.OUCH, "Me dolió"),
        (Type.SORRY, "Me hago cargo"),
    ]

    poster = ForeignKey(Poster)
    type   = CharField(max_length=10, choices=TYPE_CHOICES)
    author = CharField(max_length=128, default='')
    text   = TextField()
    votes  = IntegerField(default=0)
