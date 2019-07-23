
from django.shortcuts import render
from django.views.generic import ListView
import quotesform.views
from django.urls import path

#from .models import QuoteCategory
from .models import Quote
# Create your views here.


class quotesview(ListView):
    template_name = "quotes.html"
    model = Quote


    # def get_queryset(self):
    #     query_set = super().get_queryset()
    #     return query_set.select_related('quote_category')

