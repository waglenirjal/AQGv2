from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.groups.all()[0].name in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('YOu are not allowed.')
        return wrap
    return decorator


def teacher_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.groups.all()[0].name == 'Teacher':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'home/t_index.html')
    return wrap


def student_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.groups.all()[0].name == 'Student':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'home/index.html')
    return wrap