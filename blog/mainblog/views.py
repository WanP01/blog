from django.core.cache import cache
from django.http import HttpResponse
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from mainblog.models import Category,Post,Tag
from config.models import SiderBar,link
from django.views.generic import ListView,DetailView,View,TemplateView
from django.db.models import Q
from comment.models import Comment
from comment.forms import CommentForm
from django.db.models import Count, F, Value


"""重写view——class-based view"""
#基础classbased view
class CommonViewMixin:
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'sidebars':SiderBar.get_all(),
            }
        )
        context.update(self.get_nav())
        return context

    def get_nav(self):
        category = Category.objects.filter(status=Category.STATUS_NORMAL)
        nav_category = []
        normal_category = []
        for cate in category:
            if cate.is_nav:
                nav_category.append(cate)
            else:
                normal_category.append(cate)
        return {
            'nav_category': nav_category,
            'normal_category': normal_category,
        }

class IndexView(CommonViewMixin,ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

    # def get(self,request,*args,**kwargs):
    #     response = super().get(request,*args,**kwargs)
    #     print(request.GET)
    #     print(request.path)
    #     return response
    # def get_ordering(self):
    #     sort = self.kwargs.get('sort',None)
    #     if sort:
    #         return ('-pv','-created_time','-id')
    #     return ('-created_time','-pv')





class CategoryView(IndexView):
    def get_context_data(self,**kwargs):
        '''增加需要传递到html的参数表Category'''
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category,pk=category_id)
        context.update(
            {
              'category':category,
            }
        )
        return context

    def get_queryset(self):
        '''重写查询（此时有category_id 附加要求），根据分类筛选'''
        category_id = self.kwargs.get('category_id')
        queryset = super().get_queryset().filter(category_id=category_id)
        return queryset

class TagView(IndexView):
    def get_context_data(self,**kwargs):
        '''增加需要传递到html的参数表Tag'''
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag,pk=tag_id)
        context.update(
            {
                'tag':tag,
            }
        )
        return context

    def get_queryset(self):
        '''重写查询（此时有tag_id 附加要求），根据标签筛选'''
        tag_id = self.kwargs.get('tag_id')
        queryset = super().get_queryset().filter(tag=tag_id)
        return queryset

"""重写view——class-based view"""

"""view——function view"""
# Create your views here.
# #返回根据category_id & tag_id 筛选出来的文章列表（没有id就显示首页）
# #排除删掉的列表 statu.normal_status
# #添加导航列表内容
# def post_list(request,category_id=None,tag_id=None):
#     tag = None
#     category = None
#     if tag_id:
#         tag,post_list = Post.get_by_tag(tag_id=tag_id)
#     elif category_id:
#         category,post_list = Post.get_by_category(category_id=category_id)
#     else:
#         post_list = Post.latest_posts()
#
#     context = {
#         'category':category,
#         'tag': tag,
#         'post_list':post_list,
#         'siderbars':SiderBar.get_all(),
#     }
#
#     context.update(Category.get_nav())
#     return render(request,'blog/list.html',context=context)
#
#
#     # content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(category_id=category_id,tag_id=tag_id)
#     # # content = f'post_list category_id={category_id}, tag_id={tag_id}'
#     # return HttpResponse(content)
"""view——function view"""

"""重写view——class-based view"""
class PostDetailView(CommonViewMixin,DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get(self,request,*args,**kwargs):
        response = super().get(request,*args,**kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid
        pv_key = 'pv:%s:%s' %(uid,self.request.path)
        uv_key = 'uv:%s:%s:%s' %(uid,str(date.today()),self.request.path)

        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key,1,1*60)

        if not cache.get(uv_key):
            increase_uv = True
            cache.set(uv_key, 1, 24*60*60)

        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1,uv=F('uv')+1)
        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update( uv=F('uv') + 1)



    #集成在comment_block tag
    # def get_context_data(self,**kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #
    #     context.update(
    #         {
    #             'comment_form':CommentForm,
    #             'comment_list':Comment.get_by_target(self.request.path),
    #         }
    #     )
    #     return context
"""重写view——class-based view"""

"""view——function view"""
# def post_detail(request,post_id):
#     try:
#         post=Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#     # return HttpResponse('detail')
#     context = {
#         'post':post,
#     }
#     context.update(Category.get_nav())
#     return render(request,'blog/detail.html',context)
"""view——function view"""

#搜寻符合搜索框的文章list
class SearchView(IndexView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'keyword':self.request.GET.get('keyword','')}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword)|Q(desc__icontains=keyword))

#搜寻单一作者名下的文章list
class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)


