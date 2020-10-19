from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from pyuploadcare.dj.forms import ImageField

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"First Name"}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Last Name"}))
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Username"}))
    email = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Email"}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class":"form-control",
                                                                "placeholder":"Password"}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class":"form-control",
                                                                "placeholder":"Confirm Password"}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2',)

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"First Name"}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Last Name"}))
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Username"}))
    email = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Email"}))
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image_url','bio']

