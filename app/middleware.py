from django.contrib import auth

from .models import User


def AutoUserMiddleware(get_response):
    def middleware(request):
        if request.user.is_anonymous:
            user = User.objects.create()
            auth.login(request, user)

        return get_response(request)

    return middleware

