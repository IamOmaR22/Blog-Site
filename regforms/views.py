from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from .forms import registrationform
def signup(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user=User.objects.create_user(username=username,email=email, password=raw_password)
            user.set_password(raw_password)
            user.is_active=True
            user.save()
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('UserProfile')
        else:
            return render(request, 'regforms.html', {'frm': form})

    else:
        form = registrationform()
    return render(request,'regforms.html', {'frm': form})