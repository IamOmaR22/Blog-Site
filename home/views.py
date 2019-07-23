from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import photo, article

class indexview(ListView):
    template_name = "index.html"
    model = photo


# class aboutview(TemplateView):
# # #     template_name = "about.html"