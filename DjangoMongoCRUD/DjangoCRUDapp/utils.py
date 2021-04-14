from typing import Type

from djongo import models
from fastapi import Header
from fastapi import HTTPException
from fastapi import Path

from DjangoCRUDapp.models import Artista


def get_object(
    model_class: Type[models.Model],
    name: str,
) -> models.Model:

    instance = model_class.objects.filter(nombre__contains=name).first()
   
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance

def get_artist(
    name: str = Path(..., description="Nombre del artista"),
):
    return get_object(Artista, name)