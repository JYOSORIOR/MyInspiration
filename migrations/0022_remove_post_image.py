# Generated by Django 3.2.5 on 2022-05-16 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myinspiration', '0021_auto_20220516_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
