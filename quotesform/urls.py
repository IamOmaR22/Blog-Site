import quotes.views
import quotesform.views
from django.urls import path

import UserProfile.views

urlpatterns = [

    path('quotes/',quotes.views.quotesview.as_view(),name="quotes"),

    #path('UserPofile/',UserProfile.views.userview.as_view(),name="UserProfile")

]