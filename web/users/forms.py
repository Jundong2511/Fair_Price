from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# the class UserRegisterForm is a child of class UserCreationForm which
# is import from django.contrib.auth.forms, that's a basic form made by
# django, it include a lot things like uername and passcode.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # need figir Meta later
    class Meta:
        # django premade model "User".
        model = User
        # has password1 and password2 to make sure user type twice same password
        # when they register.
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
