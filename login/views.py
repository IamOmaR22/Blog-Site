from django.shortcuts import render,HttpResponse,redirect,reverse,HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from .forms import Loginuser
from django.views.generic import View
from django.contrib.auth import authenticate,login
from django.urls import path

from django.contrib import admin

def loginview(request):
    form=Loginuser(request.POST or None)
    if request.method=='GET':
        return render(request,'login.html',{'form':form})
    elif request.method=='POST':
        form = Loginuser(request.POST or None)
        if form.is_valid():
         username=form.cleaned_data.get('username')
         password=form.cleaned_data.get('password')
         user=authenticate(username=username,password=password)
         if user is not None:
             if user.is_superuser:
                 return redirect('admin:index')
             elif user.is_active:
                 login(request,user)
                #return redirect()
                 return redirect('UserProfile')


    else:
        return render(request, 'login.html', {'form': form})

