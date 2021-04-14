from typing import Optional
from pydantic import BaseModel

''' -------------------- Modelos -------------------- '''

class Artist(BaseModel):
	nombre: str
	genero: str
	subgenero: str
	decada: str
	canciones: list

class Song(BaseModel):
	metadata: dict
	cancion: list