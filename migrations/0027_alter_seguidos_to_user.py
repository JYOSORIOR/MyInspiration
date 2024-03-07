# Generated by Django 3.2.5 on 2022-05-26 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myinspiration', '0026_auto_20220523_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguidos',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_seguido+', to=settings.AUTH_USER_MODEL),
        ),
    ]