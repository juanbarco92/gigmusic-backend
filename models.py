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

	def asdict(self):
		return {
			'nombre' : self.nombre,
			'genero' : self.genero,
			'subgenero' : self.subgenero,
			'decada' : self.decada,
			'canciones' : self.canciones
		}

class Song(BaseModel):

	metadata: dict
	cancion: list

	def asdict(self):
		return {
			'metadata' : self.metadata,
			'cancion' : self.cancion,
		}


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