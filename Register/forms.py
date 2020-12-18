from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from Register.models import UserDetail
from django.forms.widgets import Input

class UserRegisterForm(UserCreationForm):
    date = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    father = forms.CharField()
    mother = forms.CharField()
    plus2name = forms.CharField()
    plus2board = forms.CharField()
    plus2year = forms.CharField()
    plus2percent = forms.CharField()
    slcname = forms.CharField()
    slcboard = forms.CharField()
    slcyear = forms.CharField()
    slcpercent = forms.CharField()
    role = forms.ModelChoiceField(queryset=Group.objects.filter(id=2))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date', 'address', 'phone',
                  'father', 'mother',
                  'plus2name', 'plus2board', 'plus2year', 'plus2percent',
                  'slcname', 'slcboard', 'slcyear', 'slcpercent', 'role')

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


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']



class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['dob', 'address', 'phone', 'father', 'mother',
                  'plus2name', 'plus2board', 'plus2year', 'plus2percent',
                  'slcname', 'slcboard', 'slcyear', 'slcpercent', 'image']

