from django.contrib import admin
from .models import *

# Register your models here.
from home import models
# admin.site.register(models.baseInfo)
# admin.site.site_header = '智城后台管理'
admin.site.site_title="辉达IT外包后台"
admin.site.index_title="辉达IT外包后台"

#公司信息表
class baseInfoAdmin(admin.ModelAdmin):
    list_display = ('email','email',)
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self,request,obj=None):
        return False
admin.site.register(models.baseInfo,baseInfoAdmin)


#轮播图片
class lunboAdmin(admin.ModelAdmin):
    list_display = ('name','img')
admin.site.register(models.lunbo,lunboAdmin)

#经典案例
class anliAdmin(admin.ModelAdmin):
    list_display = ('name','img',)
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self,request,obj=None):
        return False
admin.site.register(models.anli,anliAdmin)

#模板图片
class mubanAdmin(admin.ModelAdmin):
    list_display = ('name','img')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self,request,obj=None):
        return False
admin.site.register(models.muban,mubanAdmin)

#主营业务
class yewuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self,request,obj=None):
        return False
admin.site.register(models.yewu,yewuAdmin)

#解决方案
class fanganAdmin(admin.ModelAdmin):
    list_display = ('name','img',)
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self,request,obj=None):
        return False
admin.site.register(models.fangan,fanganAdmin)


#解决方案
class opinionAdmin(admin.ModelAdmin):
    list_display = ('username','phone','content')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self,request,obj=None):
        return False
admin.site.register(models.opinion,opinionAdmin)