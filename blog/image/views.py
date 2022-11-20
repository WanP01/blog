from django.core.files.storage import default_storage
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Image


def image(request):

    if request.method == 'GET':
        return render(request,'Image.html')
    if request.method == 'POST':
        pic = request.FILES.get('avatar')
        image = Image.objects.get(id=1)
        image.pic=pic
        image.save()
        # default_storage.save('/home/wanpeng/Desktop/django_blackhorse/django_blog/blog/media',pic)
        return None