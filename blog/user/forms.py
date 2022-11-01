import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field
from django import forms
from .models import UserInfo

class RegisterForms(forms.ModelForm):

    username = forms.CharField(
        label='姓名',
        min_length=4,
        max_length=50,
        widget=forms.TextInput,
    )

    email = forms.CharField(
        label='电子邮箱',
        min_length=4,
        max_length=50,
        widget=forms.EmailInput,
    )

    phone = forms.CharField(
        label='手机号码',
        min_length=11,
        max_length=50,
        widget=forms.NumberInput,
    )

    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=16,
        widget=forms.PasswordInput,
    )

    password_confirm = forms.CharField(
        label='确认密码',
        min_length=8,
        max_length=16,
        widget=forms.PasswordInput,
    )

    class Meta:
        model=UserInfo
        fields = ['username','email','phone','password','password_confirm']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            # field.widget.attrs.update({'class':'form-control ','placeholder':'请输入%s'%field.label,'style':'width:30%;'})
            field.widget.attrs.update(
                {'class': 'form-control '})

    def clean_username(self):
        post_username = self.cleaned_data['username']

        if UserInfo.objects.filter(username=post_username):
            raise forms.ValidationError('名称已注册')
        return post_username

    def clean_email(self):
        post_email = self.cleaned_data['email']
        if UserInfo.objects.filter(email=post_email):
            raise forms.ValidationError('邮箱已注册')
        return post_email

    def clean_phone(self):
        post_phone = self.cleaned_data['phone']
        if UserInfo.objects.filter(phone=post_phone):
            raise forms.ValidationError('手机号已注册')
        return post_phone

    #密码强度验证正则表达式
    psw_re = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}$'


    def clean_password(self):
        post_password = self.cleaned_data['password']
        if not re.match(self.psw_re,post_password):
            raise forms.ValidationError('密码不符合规范，8-16位，密码需包含数字，大写和小写字母！')
        return post_password



    def clean_password_confirm(self):
        post_password_confirm = self.cleaned_data['password_confirm']
        #这一步是为了让上下password 和 password confirm 都能报错 密码格式不对
        try:
            post_password = self.cleaned_data['password']
        except Exception as e:
            raise forms.ValidationError('密码不符合规范，8-16位，密码需包含数字，大写和小写字母！')
        else:
            if post_password != post_password_confirm:
                raise forms.ValidationError('密码不一致')
        return post_password_confirm

        # self.helper = FormHelper()
        # Fields = []
        #
        # for name,field in self.fields.items():
        #     Fields.append(Field(name,css_class='form-control item',placeholder='请输入%s'%field.label))
        #
        # self.helper.layout = Layout(
        #     Div(
        #         HTML('<span><i class="icon icon-user"></i></span>'),
        #         css_class='form-icon'
        #     ),
        #     #
        #     *Fields,
        #     Field('username', css_class='form-control item', placeholder='请输入')
        # )

class LoginForms(forms.ModelForm):

    account = forms.CharField(
        label='账号',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':"用户名 or Email or 手机号"}),
        # error_messages='该用户不存在'
    )

    password = forms.CharField(
        label='密码',
        min_length=4,
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder':'请输入密码'}),
    )


    class Meta:
        model=UserInfo
        fields = ['account','password',]



    # numregex = r'^1\d{10}$'
    # emaregex = r'\w+@\w+.com'
    #
    # def clean_account(self):
    #     account=self.cleaned_data['account']
    #     if account.isdigit() and re.match(self.numregex,account):
    #         phone = re.match(self.numregex,account).group()
    #         userobj=UserInfo.objects.filter(phone=phone)
    #     elif re.match(self.emaregex,account):
    #         email = re.match(self.emaregex,account).group()
    #         userobj = UserInfo.objects.filter(email=email)
    #     else:
    #         userobj = UserInfo.objects.filter(username=account)
    #
    #     if not userobj:
    #         raise forms.ValidationError('未找到该用户，请重试')
    #
    #     return userobj
    #
    #
    # def clean_password(self,):
    #     password=self.cleaned_data['password']
    #     userobj = self.cleaned_data['account']
    #
    #     password









