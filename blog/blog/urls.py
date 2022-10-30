"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter




from blog.settings import develop
from blog.view import TemView
from mainblog.admin import cust_site
# from mainblog.views import post_list,post_detail,links
from mainblog.views import IndexView,CategoryView,TagView,PostDetailView,SearchView,AuthorView
from comment.views import CommentView
from config.views import LinksView
from mainblog.rss import LatestPostFeed
from mainblog.sitemap import PostSitemap
from django.contrib.sitemaps import views as sitemap_views
from blog.autocomplete import CategoryAutocomplete,TagAutocomplete




# urlpatterns = [
#
#     re_path(r'^$',post_list,name='index'),
#     re_path(r'^category/(?P<category_id>\d+)/$',post_list,name='category-list'),
#     re_path(r'^tag/(?P<tag_id>\d+)/$',post_list,name='tag-list'),
#     re_path(r'^post/(?P<post_id>\d+).html$',post_detail,name='post-detail'),
#     re_path(r'^links/$',links,name='links'),
#     re_path(r'^superadmin/', admin.site.urls,name='super-admin'),
#     re_path(r'^admin/',cust_site.urls,name='admin'),
# ]
#
# from mainblog.apis import PostViewSet
# router = DefaultRouter()
# router.register(r'post',PostViewSet,)

urlpatterns = [

    re_path(r'^$',IndexView.as_view(),name='index'),
    re_path(r'^search/$',SearchView.as_view(),name='search'),
    re_path(r'^author/(?P<owner_id>\d+)/$',AuthorView.as_view(),name='author'),
    re_path(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(),name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name='tag-list'),
    re_path(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(),name='post-detail'),
    re_path(r'^links/$',LinksView.as_view(),name='links'),
    re_path(r'^comment/$',CommentView.as_view(),name='comment'),
    re_path(r'^superadmin/', admin.site.urls,name='super-admin'),
    re_path(r'^admin/',cust_site.urls,name='admin'),
    re_path(r'^rss|feed/',LatestPostFeed(),name='rss'),
    re_path(r'^sitemap\.xml$',sitemap_views.sitemap,{'sitemaps':{'post':PostSitemap}}),
    re_path(r'^category-autocomplete/$',CategoryAutocomplete.as_view(),name='category-autocomplete'),
    re_path(r'^tag-acutocomplete/$',TagAutocomplete.as_view(),name='tag-autocomplete'),
    re_path(r'^ckeditor/',include('ckeditor_uploader.urls')),
    # re_path(r'^api/post/',post_list,name='post_list'),
    # # re_path(r'^api/post/',PostList.as_view(),name='post_list')
    # re_path(r'^api/',include(router.urls))
    re_path(r'^user/',include(('user.urls','user'),namespace='user')),

    re_path(r'tem/',TemView,name='tem'),



] + static(develop.MEDIA_URL,document_root=develop.MEDIA_ROOT)


if develop.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/',include(debug_toolbar.urls)),
    ] + urlpatterns