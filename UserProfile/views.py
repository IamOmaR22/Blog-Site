from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from django.contrib.auth.models import User

from django.shortcuts import render
from django.views.generic import ListView
import quotesform.views
from django.urls import path

#from .models import QuoteCategory

# Create your views here.

class userview(ListView):
    template_name = "userprofile.html"
    model = User



