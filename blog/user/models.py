from django.db import models

# Create your models here.

#改写django 自带的 User 类
from django.contrib.auth.models import AbstractUser
#设置settings.AUTH_USER_MODEL = '应用名.类名'
# username,password,email,first_name,last_name,is_superuser,is_staff,is_active,last_login,date_joined
#user = authenticate(username=username,password=password)
#set_password('password')
#login(request,user) 保持登录状态，存session
# login_required,装饰器验证登录，未登录跳转指定地址 settings.LOGIN_URL
# logout(request) 登录状态取消

class UserInfo(AbstractUser):

    default_sign = "这里什么都没有"


    # 在django 自带的User类里面增加手机号，昵称，头像，签名，简介和更新时间
    phone = models.CharField(max_length=11,default='')
    nickname = models.CharField(max_length=11,verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatar',null=True)
    sign = models.CharField(max_length=50,verbose_name='签名',default=default_sign)
    info = models.CharField(max_length=150,verbose_name='个人简介',default='')
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name=verbose_name_plural='用户信息'
        #db_table = '数据库名字'

    def __str__(self):
        return self.username
