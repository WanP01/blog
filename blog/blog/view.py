

from django.http import HttpResponse
from django.shortcuts import render

def TemView(request):
    return render(request,'tem-html.html')
