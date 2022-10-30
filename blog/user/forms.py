import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field
from django import forms
from .models import UserInfo

class RegisterForms(forms.ModelForm):

    username = forms.CharField(
        label='姓名',
        max_length=50,
        widget=forms.TextInput,
    )

    email = forms.CharField(
        label='电子邮箱',
        max_length=50,
        widget=forms.EmailInput,
    )

    phone = forms.CharField(
        label='手机号码',
        max_length=50,
        widget=forms.NumberInput,
    )

    password = forms.CharField(
        label='密码',
        min_length=4,
        max_length=50,
        widget=forms.PasswordInput,
    )

    password_confirm = forms.CharField(
        label='确认密码',
        max_length=50,
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









