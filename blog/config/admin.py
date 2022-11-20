from django.contrib import admin
from .models import link,SiderBar
# Register your models here.
@admin.register(link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','href','weight','status','owner','created_time')
    fields = ('title','href','status','weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request,obj,form,change)

@admin.register(SiderBar)
class SiderBarAdmin(admin.ModelAdmin):
    list_display = ('title','display_type','content','created_time')
    fields = ('title','display_type','content')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request,obj,form,change)