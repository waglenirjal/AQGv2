from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def indexNView(request):
    return render(request, 'home/index.html')


# def indexNView(request):
#     if request.method == 'GET':
#         role = request.user.groups.all()[0].name
#         if role == 'Teacher':
#             return render(request, 'register/register.html')
#         elif role == 'Student':
#             return render(request, 'register/register.html')
#         else:
#             return render(request, 'register/register.html')