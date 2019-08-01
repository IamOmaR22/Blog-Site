from django.shortcuts import render,redirect
from quotes.models import Quote#, QuoteCategory
from django.urls import path
from django.views.generic import TemplateView
# Create your views here.
# class quotesformview(TemplateView):
#     template_name = "quotesform.html"
#     from django.shortcuts import render
#     from .models import Post

# How to insert data into a database from an HTML form in Django
def quotesformview(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('person') and request.POST.get('quote'):
            quote = Quote()
            #quote_cate = QuoteCategory()
            quote.title = request.POST.get('title')
            quote.author = request.POST.get('person')
            quote.quote = request.POST.get('quote')
            quote.save()
            #quote_cate.save()
            return redirect('quotes')
    else:
        return render(request, 'quotesform.html')