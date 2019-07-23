from django.urls import path
from .import views
import regforms.views
import login.views
import quotes.views
import quotesform.views
import UserProfile.views

urlpatterns = [
    path('',views.indexview.as_view() ,name="index"),
    path('about/',views.aboutview.as_view(),name="about"),
    path('signup/',regforms.views.signup,name="signup"),
    path('login/',login.views.loginview,name="login"),
    path('quotes/',quotes.views.quotesview.as_view(),name="quotes"),
    #path('UserPofile/',UserProfile.views.userview.as_view(),name="UserProfile")

]