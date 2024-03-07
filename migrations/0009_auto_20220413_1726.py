# Generated by Django 3.2.5 on 2022-04-13 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myinspiration', '0008_auto_20220413_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Enter owner's first name", max_length=50)),
                ('last_name', models.CharField(help_text="Enter owner's last name", max_length=50)),
                ('email', models.EmailField(blank=True, help_text="Enter owner's email", max_length=50, unique=True)),
                ('phone_number', models.CharField(blank=True, help_text="Enter owner's phone number", max_length=15, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
