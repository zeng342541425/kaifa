# Generated by Django 2.0 on 2018-11-28 08:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20181128_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='muban',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='内容'),
        ),
    ]
