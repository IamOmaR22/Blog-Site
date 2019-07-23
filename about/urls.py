import quotesform.views
from django.urls import path
from .import views

urlpatterns = [
    path('about',views.aboutview.as_view() ,name="about"),

]