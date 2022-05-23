from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)


    def __str__(self):
        return f'Perfil de {self.user.username}'

    def siguiendo(self):
        user_ids = Seguidos.objects.filter(from_user = self.user\
                                            .values_list('to_user_id', flat =True))
        return User.objects.filter(id__in=user_ids)

    def seguidores(self):
        user_ids = Seguidos.objects.filter(to_user = self.user\
                                            .values_list('from_user_id', flat =True))
        return User.objects.filter(id__in=user_ids)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'


#followers
class Seguidos(models.Model):
    from_user = models.ForeignKey(User, related_name= 'usuario', on_delete= models.CASCADE)
    to_user = models.ForeignKey(User, related_name= 'usuario_seguido', on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes = [

            models.Index(fields = ['from_user', 'to_user']),

        ]