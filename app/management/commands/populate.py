from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.db import transaction

from app.models import *


LOREM_WORDS = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".split()


class Command(BaseCommand):
    help = 'Populate database with example models'

    @transaction.atomic
    def handle(self, *args, **options):
        p1 = Poster.objects.create(
            text = "Manejás como mujer"
        )

        p2 = Poster.objects.create(
            text = "No seas histérica"
        )

        p3 = Poster.objects.create(
            text = "Las minas no saben nada de asado"
        )

        Comment.objects.create(
            type   = Comment.Type.OUCH,
            poster = p1,
            author = "",
            text   = LOREM_WORDS[:10]
        )

        Comment.objects.create(
            type   = Comment.Type.OUCH,
            poster = p1,
            author = "Agustina",
            text   = LOREM_WORDS[:20]
        )

        Comment.objects.create(
            type   = Comment.Type.SORRY,
            poster = p3,
            author = "Carlos",
            text   = LOREM_WORDS[:30]
        )


