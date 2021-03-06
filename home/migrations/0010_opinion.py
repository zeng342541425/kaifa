# Generated by Django 2.0 on 2018-11-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_lunbo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True, verbose_name='姓名')),
                ('phone', models.CharField(max_length=2000, null=True, verbose_name='电话')),
                ('content', models.TextField(max_length=2000, null=True, verbose_name='提交内容')),
            ],
            options={
                'verbose_name': '意见提交',
                'verbose_name_plural': '意见提交',
            },
        ),
    ]
