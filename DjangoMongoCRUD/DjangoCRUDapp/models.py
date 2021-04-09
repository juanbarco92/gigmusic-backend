#Python
from typing import Any, Dict, List
from pydantic import BaseModel
from datetime import date
from djongo import models

#Django
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Artista(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    subgenero = models.CharField(max_length=20, blank=True)
    decada = models.CharField(max_length=20, blank=True)
    canciones = models.JSONField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name   

# FastApi "MODEL"

class ArtistaAPI(BaseModel):
    
    nombre: str
    genero: str
    subgenero: str
    decada: str
    canciones: dict
    start_date: date
    end_date: date    

    @classmethod
    def from_model(cls, instance: Artista):

        return cls(
            nombre=instance.nombre,
            genero=instance.genero,
            subgenero=instance.subgenero,
            decada=instance.decada,
            canciones=instance.canciones,
            start_date=instance.start_date,
            end_date=instance.end_date,            
        )

class ArtistaAPIS(ArtistaAPI):
    id: str