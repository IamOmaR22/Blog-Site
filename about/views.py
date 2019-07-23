import quotesform.views
from django.urls import path
from django.contrib.auth.models import User

from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import about


class aboutview(ListView):
    template_name = "about.html"
    model = about

