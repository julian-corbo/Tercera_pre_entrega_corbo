from django.contrib import admin
from django.urls import path

from perfiles.views import  signup, login_view, CustomLogoutView

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),


]