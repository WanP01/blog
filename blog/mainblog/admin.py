
from django.contrib import admin

from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
from .adminforms import PostAdminForm
from .models import Category,Post,Tag
from blog.custom_admin import cust_site
from blog.base_admin import BaseAdmin



#内置关连数据修改项
class PostInline(admin.TabularInline):
    fields = ('title','desc')
    extra = 1
    model = Post


#重新定义右侧栏的过滤器
class CategoryQwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset



@admin.register(Category,site=cust_site)
class CategoryAdmin(BaseAdmin):
    inlines = (PostInline,)
    list_display = ('name','status','is_nav','created_time','owner')
    fields = ('name','status','is_nav')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin,self).save_model(request,obj,form,change)

    @admin.display(description='文章数量')
    def post_count(self,obj):
        return obj.post_set().Count()

@admin.register(Tag,site=cust_site)
class TagAdmin(BaseAdmin):
    list_display = ('name','status','created_time','owner')
    fields = ('name','status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     super().save_model(request, obj, form, change)



@admin.register(Post,site=cust_site)
class PostAdmin(BaseAdmin):
    form = PostAdminForm
    list_display = ('title','category','status','created_time','operator','owner')
    list_display_links = ()

    list_filter = (CategoryQwnerFilter,)
    search_fields = ('title','category__name')

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True


    # fields = (('category','title'),'desc','status','content','tag')
    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('title','status'),
                ('tag','category',),
            ),
        }),

        ('内容',{
            'fields':(
                'desc',
                'content',
                'is_md',
                'content_md',
                'content_ck',
            )
        }),

        # ('额外信息',{
        #     'classes':('collapse',),
        #     'fields':('tag',),
        # }),

    )

    # @admin.display(description='操作')
    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # obj.id
            # reverse('cust_admin:mainblog_post_change',args = (obj.id,))
            reverse('cust_admin:mainblog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     super().save_model(request, obj, form, change)
    #
    #
    #
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(owner=request.user)

# admin.site.register(Post,PostAdmin)

    # class Media:
    #     js =('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js','js/post_editor.js',)
    #     # css = {
    #     # 'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
    #     # }


