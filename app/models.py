# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from slugify import slugify

from django.db.models import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        return super(Poster, self).save(*args, **kwargs)


class Comment(Model):
    class Type:
        OUCH  = 'ouch'
        SORRY = 'sorry'

    TYPE_CHOICES = [
        (Type.OUCH, "Me dolió"),
        (Type.SORRY, "Me hago cargo"),
    ]

    poster = ForeignKey(Poster, related_name='comments')
    type   = CharField(max_length=10, choices=TYPE_CHOICES)
    author = CharField(max_length=128, default='')
    text   = TextField()
    votes  = IntegerField(default=0)
