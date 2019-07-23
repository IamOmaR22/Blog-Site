
from django.contrib.auth import get_user_model,authenticate,login,logout
from . import views
from django import forms
from django.shortcuts import render
from django.core.exceptions import ValidationError
class Loginuser(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    # def clean(self,*args,**kwargs):
    #     username=self.cleaned_data.get('username')
    #     password=self.cleaned_data.get('password')
    #     user= authenticate(username=username,password=password)
    #     if not user:
    #         raise ValidationError('Username does not exist')
    #     if not user.check_password(password):
    #         raise ValidationError("Password incorrect")
    #     return render ('login.html')
    #
