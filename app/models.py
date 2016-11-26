# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from slugify import slugify

from django.db import transaction
from django.db.models import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create(self):
        return super(UserManager, self).create(uuid=str(uuid.uuid4()), password='asd')

    def create_user(self, uuid, password=None):
        User.objects.create(uuid=str(uuid), password=password)

    def create_superuser(self, uuid, password=None):
        return self.create_user(str(uuid), password)


class User(AbstractBaseUser):
    objects = UserManager()

    USERNAME_FIELD = 'uuid'
    uuid = CharField(max_length=36, unique=True)


class Poster(Model):
    slug = CharField(max_length=256, unique=True)
    text = CharField(max_length=256)

    @transaction.atomic
    def react(self, user, type):
        return Reaction.objects.get_or_create(poster=self, author=user, type=type)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        return super(Poster, self).save(*args, **kwargs)


class Reaction(Model):
    class Type:
        OUCH  = 'ouch'
        SORRY = 'sorry'

        CHOICES = [
            (OUCH, "ouch"),
            (SORRY, "sorry"),
        ]

    class Meta:
        unique_together = [('poster', 'author')]

    poster = ForeignKey(Poster, related_name='reactions')
    author = ForeignKey(User, related_name='reactions')
    type   = CharField(max_length=10, choices=Type.CHOICES)


class Comment(Model):
    reaction = OneToOneField(Reaction, related_name='comment')
    text     = TextField()
    votes    = IntegerField(default=0)
