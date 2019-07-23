import quotesform.views
from django.urls import path
from .import views

urlpatterns = [
    path('UserProfile',views.userview.as_view() ,name="UserProfile"),
    path('quotesform/', quotesform.views.quotesformview, name="quotesform"),

]