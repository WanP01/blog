import re

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import View
from .forms import RegisterForms
from django.views import generic
from user.models import UserInfo
from user.forms import RegisterForms,LoginForms





# Create your views here.
class UserLogin(generic.ListView):
    model = UserInfo
    template_name = 'user/login.html'

    #验证account的正则表达式（用户名，手机号码, Email）
    numregex = r'^1\d{10}$'
    emaregex = r'\w+@\w+.com'

    def get(self,request,*args, **kwargs):
       # response = super().get(request,*args, **kwargs)
       userforms = LoginForms()
       context = {
           # "request":request,
           "form":userforms,
       }
       return render(request,self.template_name,context)

    def post(self,request,*args, **kwarg):
        userforms=LoginForms(request.POST)

        #先验证基本数据长度
        if userforms.is_valid():
            #验证密码分两步：
            #1.验证账号是否存在：
            #区分不同账号类型（username，Email，Phone）
            account=userforms.cleaned_data['account']
            if account.isdigit() and re.match(self.numregex,account):
                phone = re.match(self.numregex,account).group()
                userobj=UserInfo.objects.filter(phone=phone)
            elif re.match(self.emaregex,account):
                email = re.match(self.emaregex,account).group()
                userobj = UserInfo.objects.filter(email=email)
            else:
                userobj = UserInfo.objects.filter(username=account)
            #不存在就生成错误提示
            if not userobj:
                message="账号不存在,请重试!"
                # pass
            #存在账号则进入到密码验证（在register部分会规定每个账号数值只有一个，所以这里只有有一个或没有两种情况）
            else:
                user_password = userobj.get('password',None)
                post_password = userforms.cleaned_data['password']
                if user_password == post_password:
                    return HttpResponseRedirect(reverse('index'))
                else:
                    message = "用户名或密码错误，请重试!"
                    # pass

            context = {
                'form':userforms,
                'message1':message,
            }
        return render(request,self.template_name,context)


class UserRegister(generic.ListView):

    model = UserInfo
    template_name = 'user/register.html'

    def get(self,request,*args, **kwargs):
        userforms=RegisterForms()
        context = {
            "form":userforms,
        }
        return render(request,self.template_name,context)
    def post(self,request,*args, **kwargs):
        pass


