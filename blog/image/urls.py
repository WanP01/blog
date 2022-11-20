
from django.urls import path


from image.views import image

urlpatterns = [
    path('',image,name='image'),
]