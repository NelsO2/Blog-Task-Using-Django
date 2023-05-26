from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

 
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


        username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your username', 'class':'form-control'}))
        email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'your Email Address', 'class':'form-control'}))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Create Password', 'class':'form-control'}))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password', 'class':'form-control'}))