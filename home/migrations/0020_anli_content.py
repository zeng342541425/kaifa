# Generated by Django 2.0 on 2018-11-28 06:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_anli_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='anli',
            name='content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='内容'),
        ),
    ]
