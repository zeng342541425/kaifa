# Generated by Django 2.0 on 2018-11-28 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20181128_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anli',
            name='content',
        ),
    ]
