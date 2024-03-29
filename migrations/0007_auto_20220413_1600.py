# Generated by Django 3.2.5 on 2022-04-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinspiration', '0006_auto_20220412_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese su nombre', max_length=200)),
                ('apellido', models.CharField(help_text='Ingrese su apellido', max_length=200)),
                ('correo', models.EmailField(blank=True, help_text='Ingrese su email', max_length=50, unique=True)),
                ('telefono', models.CharField(blank=True, help_text='Ingrese su numero', max_length=15, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
