import uuid

from django.contrib import auth

from .models import User


def AutoUserMiddleware(get_response):
    def middleware(request):
        if request.user.is_anonymous:
            user = User.objects.create(uuid=str(uuid.uuid4()), password='asd')
            auth.login(request, user)

        return get_response(request)

    return middleware

