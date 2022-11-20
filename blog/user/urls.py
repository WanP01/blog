from django.conf.urls.static import static
from django.urls import re_path
from user.views import UserLogin,UserRegister,UserLogout,UserDetail,UserDetailChange
from blog.settings import develop

urlpatterns = [

    re_path(r'login',UserLogin.as_view(),name='login'),
    re_path(r'logout',UserLogout,name='logout'),
    re_path(r'register',UserRegister.as_view(),name='register'),
    re_path(r'^userinfo/(?P<user_id>\d+)/(?P<sort>\w+)',UserDetail.as_view(),name='userdetail'),
    re_path(r'^userinfochange',UserDetailChange.as_view(),name='userdetailchange'),
    ]