from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Image(models.Model):
    pic = models.ImageField(upload_to='avatar')