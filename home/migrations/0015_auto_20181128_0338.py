# Generated by Django 2.0 on 2018-11-28 03:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20181128_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anli',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='内容'),
        ),
    ]
