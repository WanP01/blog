from django.http import HttpResponse
from django.shortcuts import render
from .models import link
from mainblog.views import CommonViewMixin
from django.views.generic import ListView


# Create your views here.
# def links(request):
#      return HttpResponse('links')

class LinksView(CommonViewMixin,ListView):
     queryset =link.objects.filter(status=link.STATUS_NORMAL)
     template_name = 'config/links.html'
     context_object_name = 'link_list'