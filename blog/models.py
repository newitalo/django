from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('rascunho' , 'Raschunho'),
        ('publicado' , 'Publicado'),

    )
    titulo = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250)     #https://site.com/noticias/campeonato-lol
    autor  = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    conteudo  = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)
    alterado  = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                                 choices=STATUS,
                                 default='rascunho')


    class Meta:
        ordering  =  ('-publicado',)

    def  str  (self):
        return self.titulos

# Create your models here.
