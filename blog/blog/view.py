

from django.http import HttpResponse
from django.shortcuts import render
"""临时页面"""
def TemView(request):
    return render(request,'tem-html.html')
