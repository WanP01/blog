from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.custom_admin import cust_site
from user.forms import UserInfoForms
from user.models import UserInfo


# Register your models here.

# admin.site.register(UserInfo,UserAdmin)

@admin.register(UserInfo,site=cust_site)
class UserInfoAdmin(UserAdmin):
    form = UserInfoForms
    fieldsets = (
        ('基础信息', {
            'description': '基础个人信息描述',
            'fields': (
                ('username'),
                ('nickname'),
                ('phone'),
                ('email'),
            ),
        }),

        ('头像', {
            'fields': (
                'avatar',
            )
        }),

        ('个人简介', {
            'fields': (
                'sign',
                'info',
            )
        }),
    )