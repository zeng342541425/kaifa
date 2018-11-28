from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


#服务热线
class baseInfo(models.Model):
    class Meta:
        verbose_name="基本信息"
        verbose_name_plural = '基本信息'
    email=models.EmailField('邮箱')
    tel=models.CharField('tel',max_length=200,null=True)
    www=models.CharField('网址',max_length=200,null=True)
    phone=models.CharField('电话',max_length=200,null=True)
    address=models.CharField('公司地址',max_length=1000,null=True)
    gzh=models.ImageField('公众号图片',upload_to='imgs')
    wx=models.ImageField('个人微信图片',upload_to='imgs')

#轮播图
class lunbo(models.Model):
    class Meta:
        verbose_name="轮播图"
        verbose_name_plural = '轮播图'
    name=models.CharField('图片名字',null=True,max_length=200)
    img=models.ImageField('轮播图片',upload_to='imgs')

#经典案例
class anli(models.Model):
    class Meta:
        verbose_name="经典案例"
        verbose_name_plural = '经典案例'

    name=models.CharField('案例名字',null=True,max_length=200)
    intro=models.CharField('案例简介',null=True,max_length=2000)
    content = RichTextUploadingField(verbose_name=u'内容',null=True)
    img=models.ImageField('背景图片',upload_to='imgs')

#行业模板图片
class muban(models.Model):
    class Meta:
        verbose_name="模板图片"
        verbose_name_plural = '模板图片'
    name=models.CharField('模板名称',null=True,max_length=200)
    content = RichTextUploadingField(verbose_name=u'内容',null=True)
    img=models.ImageField('模板图片',upload_to='imgs')


#经典案例  
class fangan(models.Model):
    class Meta:
        verbose_name="解决方案"
        verbose_name_plural = '解决方案'
    name=models.CharField('方案标题',null=True,max_length=200)
    intro=models.CharField('方案简介',null=True,max_length=2000)
    img=models.ImageField('图片',upload_to='imgs')

#主营业务  
class yewu(models.Model):
    class Meta:
        verbose_name="主营业务"
        verbose_name_plural = '主营业务'
    name=models.CharField('业务介绍',null=True,max_length=200)
    img=models.ImageField('图片',upload_to='imgs',null=True)
    content = RichTextUploadingField(verbose_name=u'内容',null=True)

#经典案例 
class opinion(models.Model):
    class Meta:
        verbose_name="意见提交"
        verbose_name_plural = '意见提交'
    username=models.CharField('姓名',null=True,max_length=200)
    phone=models.CharField('电话',null=True,max_length=2000)
    content=models.TextField('提交内容',null=True,max_length=2000)
    