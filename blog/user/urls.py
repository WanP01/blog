from django.urls import re_path
from user.views import UserLogin,UserRegister

urlpatterns = [

    re_path(r'login',UserLogin.as_view(),name='login'),
    re_path(r'register',UserRegister.as_view(),name='register'),
    ]