# Generated by Django 3.2.5 on 2022-04-12 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myinspiration', '0002_inspiration_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inspiration',
            options={'ordering': ['-timestamp']},
        ),
    ]
