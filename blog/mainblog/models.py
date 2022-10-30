from functools import cached_property

from django.db import models

# Create your models here.
# from django.contrib.auth.models import User
from user.models import UserInfo
from django.db import models
import mistune


class Category(models.Model):

    STATUS_NORMAL = 1
    STATUS_DELETE  = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除')
    )

    #id 可以自增
    name = models.CharField(max_length=50,verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name='状态')
    is_nav = models.BooleanField(default=False,verbose_name='是否为导航')
    owner = models.ForeignKey(UserInfo,verbose_name='作者',on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'
    def __str__(self):
        return self.name
    #迁移至classbased View CommonViewMixin
    # @classmethod
    # def get_nav(cls):
    #     category = cls.objects.filter(status=cls.STATUS_NORMAL)
    #     nav_category = []
    #     normal_category = []
    #     for cate in category:
    #         if cate.is_nav:
    #             nav_category.append(cate)
    #         else:
    #             normal_category.append(cate)
    #     return {
    #         'nav_category': nav_category,
    #         'normal_category': normal_category,
    #     }

class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    name = models.CharField(max_length=50,verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name='状态')
    owner = models.ForeignKey(UserInfo,verbose_name='作者',on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        # db_table =
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    title = models.CharField(max_length=255,verbose_name='标题')
    desc = models.CharField(max_length=1024,blank=True,verbose_name='摘要')
    content = models.TextField(verbose_name='正文',help_text='正文必须为markdown格式')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL,verbose_name='状态')
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    owner = models.ForeignKey(UserInfo,verbose_name='作者',on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    content_html = models.TextField(verbose_name='正文html格式', editable=False,blank=True)

    is_md = models.BooleanField(default=False,verbose_name='Markdown语法')

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv').only('title','id')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']
    def __str__(self):
        return self.title

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.filter(id= tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner','category')

        return tag,post_list

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.filter(id= category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner','category')

        return category,post_list

    @classmethod
    def latest_posts(cls):
        post_list = cls.objects.filter(status=cls.STATUS_NORMAL).select_related('owner','category').prefetch_related('tag')
        return post_list

    def save(self,*args,**kwargs):
        if self.is_md:
            self.content_html = mistune.markdown(self.content)
        else:
            self.content_html = self.content
        super().save(*args,**kwargs)

    @cached_property
    def tags(self):
        return ','.join(self.tag.values_list('name',flat=True))

