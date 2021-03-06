# Generated by Django 2.0 on 2018-11-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseinfo',
            options={'verbose_name': '基本信息', 'verbose_name_plural': '基本信息'},
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='phone',
            field=models.CharField(max_length=200, null=True, verbose_name='电话'),
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='tel',
            field=models.CharField(max_length=200, null=True, verbose_name='tel'),
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='www',
            field=models.CharField(max_length=200, null=True, verbose_name='网址'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='gzh',
            field=models.ImageField(upload_to='imgs', verbose_name='公众号图片'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='hotLine',
            field=models.CharField(max_length=200, null=True, verbose_name='服务热线'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='wx',
            field=models.ImageField(upload_to='imgs', verbose_name='个人微信图片'),
        ),
    ]
