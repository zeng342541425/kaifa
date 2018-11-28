"""kaifa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include,re_path
from kaifa.settings import MEDIA_ROOT   #当前项目下的settings
from home import views as home_views
from django.views.static import serve
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home_views.index,name="index"),

    path('info/<int:infoid>',home_views.info,name="info"),

    path('yewu/<int:yewuid>',home_views.yewu,name="yewu"),  #主营业务详情
    path('muban/<int:mubanid>',home_views.muban,name="muban"),  #模板详情

    path('add/',home_views.add),  #提交意见

    path(r'^ckeditor/', include('ckeditor_uploader.urls')),  #编辑器

    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]

urlpatterns += static('/', document_root=settings.MEDIA_ROOT)
