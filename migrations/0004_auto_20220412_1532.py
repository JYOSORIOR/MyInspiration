# Generated by Django 3.2.5 on 2022-04-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinspiration', '0003_alter_inspiration_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inspiration',
            options={},
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]