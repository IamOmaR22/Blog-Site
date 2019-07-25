
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
from django.shortcuts import render
from .models import photo, myquote


def indexview(request):
    myqu = myquote.objects.filter()
    ph= photo.objects.filter()
    context = {'myqu':myqu, 'ph':ph}
    return render(request, 'index.html', context)







# class aboutview(TemplateView):
# # #     template_name = "about.html"
