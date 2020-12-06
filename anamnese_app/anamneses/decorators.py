from django.http import HttpResponse
from django.shortcuts import redirect


def usuario_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('Você não tem permissão para acessar esta página.')
    return wrapper_func
