import re

from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import View

from mainblog.models import Post
from .forms import RegisterForms
from django.views import generic
from user.models import UserInfo
from user.forms import RegisterForms,LoginForms,UserInfoForms
from user.tools.password_tools import pw_md5



#Create your views here.
'''登录'''
class UserLogin(View):
    template_name = 'user/login.html'

    '''验证account的正则表达式（用户名，手机号码, Email）'''
    numregex = r'^1\d{10}$'
    emaregex = r'\w+@\w+.com'

    def get(self,request):
       #response = super().get(request,*args, **kwargs)
       userforms = LoginForms()
       context = {
           #"request":request,
           "form":userforms,
       }
       return render(request,self.template_name,context)

    def post(self,request):
        userforms=LoginForms(request.POST)
        '''先验证基本数据长度'''
        if userforms.is_valid():
            '''验证密码分两步：'''
            '''1.验证账号是否存在：'''
            '''区分不同账号类型（username，Email，Phone）'''
            account=userforms.cleaned_data['account']
            if account.isdigit() and re.match(self.numregex,account):
                # phone = re.match(self.numregex,account).group()
                userobj=UserInfo.objects.filter(phone=account)
            elif re.match(self.emaregex,account):
                # email = re.match(self.emaregex,account).group()
                userobj = UserInfo.objects.filter(email=account)
            else:
                userobj = UserInfo.objects.filter(username=account)
            '''不存在就生成错误提示'''
            '''存在账号则进入到密码验证（在register部分会规定每个账号数值只有一个，所以这里只有有一个或没有两种情况,不存在两个账号）'''
            if not userobj:
                message = "账号不存在,请重试!"
                #pass

            else:
                for user in userobj:
                    post_password = userforms.cleaned_data['password']
                    #user_password = userobj.password
                    #p_p_m = pw_md5(post_password)
                    #if user_password == p_p_m:
                    #session中存入用户id,姓名，和登录状态
                    '''django 有一套验证密码的接口（密码存入django后台admin会加密）'''
                    if authenticate(username=user.username,password=post_password):
                        # request.session['user_id'] = user.id
                        request.session['user_name'] = user.username
                        request.session['is_login'] = True

                        return HttpResponseRedirect(reverse('index'))

                    else:
                        message = "用户名或密码错误，请重试!"
                        #pass

            context = {
                'form':userforms,
                'message':message,
            }
            return render(request,self.template_name,context)

'''注册'''
class UserRegister(View):

    template_name = 'user/register.html'

    def get(self,request):
        userforms=RegisterForms()
        context = {
            "form":userforms,
        }
        return render(request,self.template_name,context)


    def post(self,request):
        userforms = RegisterForms(request.POST)

        '''初步数据验证OK(包括密码强度；密码一致性；用户名，邮箱，手机号唯一性；正确格式等)'''
        if userforms.is_valid():
            '''存储加密后的密码'''
            password = userforms.cleaned_data['password']
            instance = userforms.save(commit=False)
            #instance.password = pw_md5(password)
            '''django 自身有一套加密算法加密密码 object.set_password'''
            instance.set_password(password)
            '''session中存入,姓名，和登录状态'''
            '''没有id，因为id是存进去后mysql自增的'''
            request.session['user_name'] = instance.username
            request.session['is_login'] = True


            print(instance.username)

            instance.save()
            userforms.save_m2m()
            return HttpResponseRedirect(reverse('index'))
        else:
            message = '注册失败，请重试'
        context = {
            'form':userforms,
            'message':message,
        }
        return render(request,self.template_name,context)

'''登出'''
def UserLogout(request):

    request.session.flush()

    return HttpResponseRedirect(reverse('index'))

'''用户信息'''
class UserDetail(View):

    def get(self,request,user_id,sort):

        login_id = request.user_id
        #print(type(login_id))
        #print(user_id)
        #print(str(login_id)==user_id)
        user_detail = UserInfo.objects.filter(id=user_id)

        user_blogs = None

        if sort == 'lasted':
            user_blogs = Post.latest_posts().filter(id=user_id)
        elif sort == 'hot':
            user_blogs = Post.hot_posts().filter(id=user_id)

        '''如果登录用户和要访问的用户一致，给出全部信息'''
        if str(login_id) == user_id:
            context = {
                'user_detail':user_detail,
                'is_self':True,
                'user_blogs':user_blogs,
            }
            return render(request,'user/userdetail.html',context)
        else:
            """如果登录用户和要访问的用户不一致，给出部分信息"""
            user_detail= user_detail.values('username','nickname','email','avatar','sign','info','last_login')
            context = {
                'user_detail': user_detail,
                'is_self': False,
                'user_blogs': user_blogs,
            }
            return render(request, 'user/userdetail.html', context)


class UserDetailChange(View):

    def get(self,request):

        user_de_ch_forms =UserInfoForms()
        context={
            'form':user_de_ch_forms,
        }

        return render(request, 'user/userdetailchange.html', context)



