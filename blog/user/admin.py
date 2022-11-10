from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.custom_admin import cust_site
from user.models import UserInfo


# Register your models here.

# admin.site.register(UserInfo,UserAdmin)

@admin.register(UserInfo,site=cust_site)
class UserInfoAdmin(UserAdmin):
    pass