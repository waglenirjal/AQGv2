from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from T_register.forms import TeacherRegisterForm, TeacherProfileUpdate, TeacherUpdate
from T_register.models import TeacherDetail
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from aqg.decorators import role_required, teacher_only
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def handleHome(request):
    return render(request, 'home/t_index.html')


@teacher_only
def cs(request):
    return render(request, 'comingsoon.html')

def tRegisterView(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            dob = form.cleaned_data.get('date')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            form.save()
            TeacherDetail(user=User.objects.filter(username=username).first(),
                       dob=dob, address=address, phone=phone).save()
            messages.success(request, 'Success')
        else:
            messages.error(request, 'Invalid: try again')



    else:
        form = TeacherRegisterForm()
    params = {
        'form': form,
    }
    print('---------------------------------')
    print(request.user)
    return render(request, 'register/t_register.html', params)


def handleLogin(request):
    if request.method == 'POST':
        # get the post parameters
        print('i am here ')
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']


        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully loged In')
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return redirect('handleHome')
        else:
            messages.error(request, 'Invalid: try again')
            # return redirect('handleLogin')
            return render(request, 'login/t_login.html')


    return render(request, 'login/t_login.html')

@login_required
# role_required(allowed_roles=['Teacher'])
@teacher_only
def handleLogout(request):
    logout(request)
    messages.success(request, 'Success: Log Out')
    return redirect('handleHome')




@login_required
# role_required(allowed_roles=['Teacher'])
@teacher_only
def profileTeacher(request):
    return render(request, 't_profile/profile.html')



@login_required
# role_required(allowed_roles=['Teacher'])
@teacher_only
def editProfileTeacher(request):
    if request.method == 'POST':
        u_form = TeacherUpdate(request.POST, instance=request.user)  # instance shows in field
        p_form = TeacherProfileUpdate(request.POST, request.FILES, instance=request.user.teacherdetail)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile is Updated.')
        return render(request, 't_profile/Profile.html')

    else:
        u_form = TeacherUpdate(instance=request.user)  # instance shows in field
        p_form = TeacherProfileUpdate(instance=request.user.teacherdetail)
    params = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 't_profile/editProfile.html', params)


@login_required
# role_required(allowed_roles=['Teacher'])
@teacher_only
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            v = form.save()
            update_session_auth_hash(request, v)
            messages.success(request, 'Your Password has been changed.')
            return render(request, 't_profile/profile.html')
        else:
            messages.error(request, 'No Change')

    else:
        form = PasswordChangeForm(request.user)
    params = {
        'form': form,
    }
    return render(request, 't_profile/changepass.html', params)


