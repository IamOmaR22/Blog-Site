
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
from django.shortcuts import render
from .models import photo, article


def indexview(request):
    arti = article.objects.filter()
    ph= photo.objects.filter()
    context = {'arti':arti, 'ph':ph}
    return render(request, 'index.html', context)







# class aboutview(TemplateView):
# # #     template_name = "about.html"
