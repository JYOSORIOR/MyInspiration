# Generated by Django 3.2.5 on 2022-04-24 16:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myinspiration', '0014_auto_20220424_1055'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Usuario',
        ),
    ]
