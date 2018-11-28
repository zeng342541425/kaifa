from django.http import HttpResponse
from django.shortcuts import render
from home import models
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    from home import models
    baseInfo=models.baseInfo.objects.get(id=1)   #基本信息
    lunbo=models.lunbo.objects.all()   #轮播图
    anli=models.anli.objects.all()   #轮播图
    muban=models.muban.objects.all()   #轮播图
    fangan=models.fangan.objects.all()   #轮播图
    yewu=models.yewu.objects.all()   #轮播图
    return render(request,"index.html",{'baseInfo':baseInfo,'lunbo':lunbo,'anli':anli,'muban':muban,'fangan':fangan,'yewu':yewu})

#案例详情
def info(request,infoid):
    from home import models
    anli=models.anli.objects.get(id=infoid)   #轮播图
    return render(request,"info.html",{'anli':anli})

#主营业务
def yewu(request,yewuid):
    from home import models
    yewu=models.yewu.objects.get(id=yewuid)   #轮播图
    return render(request,"yewu.html",{'yewu':yewu})

#模板详情
def muban(request,mubanid):
    from home import models
    muban=models.muban.objects.get(id=mubanid)   #轮播图
    return render(request,"muban.html",{'muban':muban})


def add(request):
    if request.method == "POST":
        username = request.POST["username"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        models.opinion.objects.create(username=username,phone=phone,content=content)
    return HttpResponseRedirect("/") 
