from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from Register.models import UserDetail
from django.forms.widgets import Input

class TeacherRegisterForm(UserCreationForm):
    date = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    role = forms.ModelChoiceField(queryset=Group.objects.filter(id=1))



    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'date', 'address', 'phone', 'role')

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        role = self.cleaned_data.pop('role')
        u = super().save()
        u.groups.set([role])
        u.save()
        return u




class TeacherUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']



class TeacherProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['dob', 'address', 'phone', 'image']

