# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.db import transaction

from app.models import *


LOREM_WORDS = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".split()


class Command(BaseCommand):
    help = 'Populate database with example models'

    @transaction.atomic
    def handle(self, *args, **options):
        u1 = User.objects.create()

        p1 = Poster.objects.create(
            text = "Con mujeres no discuto"
        )

        p2 = Poster.objects.create(
            text = "Cuidá a tu hermana que es mujer"
        )

        p3 = Poster.objects.create(
            text = "No seas minita"
        )

        p4 = Poster.objects.create(
            text = "Podés dar la clase sola?"
        )

        p5 = Poster.objects.create(
            text = "Manejás como mujer"
        )

        p6 = Poster.objects.create(
            text = "Llorás como nena"
        )

        p7 = Poster.objects.create(
            text = "No seas histérica"
        )

        # for _ in range(3):
        #     u = User.objects.create()
        #     Reaction.objects.create(poster=p1, author=u, type=Reaction.Type.OUCH)

        # for _ in range(2):
        #     u = User.objects.create()
        #     Reaction.objects.create(poster=p1, author=u, type=Reaction.Type.SORRY)

        # Comment.objects.create(
        #     reaction = p1.reactions.first(),
        #     text     = ' '.join(LOREM_WORDS[:20])
        # )

        # Comment.objects.create(
        #     reaction = p1.reactions.last(),
        #     text   = ' '.join(LOREM_WORDS[:30])
        # )


