from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.profile.save()

class Inspirations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inspiration')
    timestamp = models.DateTimeField(default=timezone.now)
    etiqueta = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

        def __str__(self):
            return f'{self.user.username}: {self.content}'

class Favoritos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
