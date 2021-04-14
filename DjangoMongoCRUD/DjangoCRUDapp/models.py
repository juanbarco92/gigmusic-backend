#Python
from typing import Any, Dict, List
from pydantic import BaseModel
from datetime import date
from djongo import models
from django import forms

#Django
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Cancion(models.Model):
    
    canción = models.CharField(max_length=50)
    album = models.CharField(max_length=50)

    class Meta:
        abstract = True

class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancion
        fields = (
            'canción', 'album'
        )

class Artista(models.Model):

    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    subgenero = models.CharField(max_length=20, blank=True)
    decada = models.CharField(max_length=20, blank=True)
    canciones = models.ArrayField(
        model_container=Cancion, 
        model_form_class=CancionForm)

    def __str__(self):
        return self.name   

# FastApi "MODEL"

class ArtistaAPI(BaseModel):
    
    nombre: str
    genero: str
    subgenero: str
    decada: str
    canciones: list

    @classmethod
    def from_model(cls, instance: Artista):

        return cls(
            nombre=instance.nombre,
            genero=instance.genero,
            subgenero=instance.subgenero,
            decada=instance.decada,
            canciones=instance.canciones,            
        )

class ArtistaAPIS(ArtistaAPI):
    id: str