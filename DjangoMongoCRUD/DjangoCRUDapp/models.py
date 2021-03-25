from djongo import models
# Create your models here.
class Artista(models.Model):

    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    subgenero = models.CharField(max_length=20, blank=True)
    decada = models.CharField(max_length=20, blank=True)
    canciones = models.JSONField()
      