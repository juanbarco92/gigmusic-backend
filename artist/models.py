from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

''' -------------------- Modelos -------------------- '''

''' Base de Datos '''

# ----- Sub Modelos

class ArtistSong(BaseModel):

	cancion: str

	def asDict(self):
		return {
			'cancion' : self.cancion,
		}


# ----- Modelos Principales

class Artist(BaseModel):

	nombre: str
	genero: str
	subgenero: str
	decada: str
	canciones: List[ArtistSong]

	def asDict(self):
		return {
			'nombre' : self.nombre,
			'genero' : self.genero,
			'subgenero' : self.subgenero,
			'decada' : self.decada,
			'canciones' : self.canciones
		}

# ----- Modelos de edicion

class ArtistEdition(BaseModel):

	nombre: Optional[str] = None
	genero: Optional[str] = None
	subgenero: Optional[str] = None
	decada: Optional[str] = None
	canciones: Optional[List[ArtistSong]] = None

	def asDict(self):
		return {
			'nombre' : self.nombre,
			'genero' : self.genero,
			'subgenero' : self.subgenero,
			'decada' : self.decada,
			'canciones' : self.canciones
		}
