from django.db import models
from datetime import datetime

class Post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=250)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.titulo