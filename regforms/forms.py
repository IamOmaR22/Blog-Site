from django.contrib.auth.models import User
from django import forms
from .models import *
from django.core.validators import validate_email
class registrationform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),required=True,max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email ID'}),
                               required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
                               required=True, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
                               required=True, max_length=50)
    class Meta():
        model=User
        fields=['username','email','password','confirm_password']

    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match= User.objects.get(username = user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already exist.")
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exist.')
        return email
    def clean_confirm_password(self):
        pas=self.cleaned_data.get('password')
        cpas= self.cleaned_data.get('confirm_password')
        MIN_LENGTH=8
        if pas and cpas and pas != cpas:
                 raise forms.ValidationError('password does not match')
        else:
            if len(pas) < MIN_LENGTH:
                raise forms.ValidationError('Password should at least %d characters and Password should not all numeric ' %MIN_LENGTH)
            if pas.isdigit():
                raise forms.ValidationError('Password should not all numeric')
