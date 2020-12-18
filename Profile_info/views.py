from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Register.forms import UserUpdate, ProfileUpdate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from aqg.decorators import student_only, role_required

# Create your views here.

@login_required
@student_only
def profileView(request):
    return render(request, 'profile/profile.html')

@login_required
@student_only
def editProfile(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance=request.user)  # instance shows in field
        p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.userdetail)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile is Updated.')
        return render(request, 'profile/profile.html')

    else:
        u_form = UserUpdate(instance=request.user)  # instance shows in field
        p_form = ProfileUpdate(instance=request.user.userdetail)
    params = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile/editProfile.html', params)


@login_required
@student_only
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            v = form.save()
            update_session_auth_hash(request, v)
            messages.success(request, 'Your Password has been changed.')
            return render(request, 'profile/profile.html')
        else:
            messages.error(request, 'No Change')

    else:
        form = PasswordChangeForm(request.user)
    params = {
        'form': form,
    }
    return render(request, 'profile/changepass.html', params)