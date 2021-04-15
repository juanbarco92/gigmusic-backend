from typing import Optional
from pydantic import BaseModel
from enum import Enum

''' -------------------- Modelos -------------------- '''

''' Base de Datos '''

class Artist(BaseModel):

	nombre: str
	genero: str
	subgenero: str
	decada: str
	canciones: list

class Song(BaseModel):

	metadata: dict
	cancion: list


''' Seleccion '''

class ArtistDB(str, Enum):

	nombre = 'nombre'
	genero = 'genero'
	subgenero = 'subgenero'
	decada = 'decada'

class SongDB(str, Enum):

	artista = 'artista'
	cancion = 'cancion'
	genero = 'genero'
	subgenero = 'subgenero'
	album = 'album'
	año = 'año'
	tonalidad = 'tonalidad'
	capo = 'capo'