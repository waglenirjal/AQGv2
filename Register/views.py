from django.shortcuts import render
from Register.forms import UserRegisterForm
from Register.models import UserDetail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.

def register(request):
    return render(request, 'register/register.html')

def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            glevel = 1
            dob = form.cleaned_data.get('date')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            father = form.cleaned_data.get('father')
            mother = form.cleaned_data.get('mother')
            plus2name = form.cleaned_data.get('plus2name')
            plus2board = form.cleaned_data.get('plus2board')
            plus2year = form.cleaned_data.get('plus2year')
            plus2percent = form.cleaned_data.get('plus2percent')
            slcname = form.cleaned_data.get('slcname')
            slcboard = form.cleaned_data.get('slcboard')
            slcyear = form.cleaned_data.get('slcyear')
            slcpercent = form.cleaned_data.get('slcpercent')
            form.save()
            UserDetail(user=User.objects.filter(username=username).first(), glevel=glevel,
                       dob=dob, address=address, phone=phone, father=father, mother=mother,
                       plus2name=plus2name, plus2board=plus2board, plus2year=plus2year, plus2percent=plus2percent,
                       slcname=slcname, slcboard=slcboard, slcyear=slcyear, slcpercent=slcpercent).save()
            messages.success(request, 'Success')

        else:
            messages.error(request, 'Invalid: try again')





    else:
        form = UserRegisterForm()


    params = {
        'form': form,
    }
    return render(request, 'register/register.html', params)