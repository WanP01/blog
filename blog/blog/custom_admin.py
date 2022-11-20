from django.contrib.admin import AdminSite

#定制site
class CustomAdmin(AdminSite):
        site_header = 'blog'
        site_title =  'blog管理后台'
        index_title = '首页'

cust_site = CustomAdmin(name='cust_admin')