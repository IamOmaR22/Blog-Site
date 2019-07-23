
from django.shortcuts import render,redirect,HttpResponse,reverse,HttpResponsePermanentRedirect
from .forms import registrationform
from django.views.generic import View
from django.contrib.auth import authenticate,login
from django.urls import path

from django.contrib import admin

from django.contrib.auth.models import User



def signup(request):
    form=registrationform(request.POST or None)
    if request.method=='GET':
        return render(request, 'regforms.html', {'form': form})
    elif request.method=='POST':
        form = registrationform(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.set_password(password)
            user.is_active = True
            user.save()
            user = authenticate(username=username, password=password, email=email)
            if user is not None:
             if user.is_active:
                login(request, user)
                return HttpResponsePermanentRedirect(reverse('UserProfile'))
                # It is the power of name and namespase

        else:
            print(form.errors)
            return render(request, 'regforms.html', {'form': form})



    else:return render(request, 'regforms.html', {'form': form})

          # user authentication



