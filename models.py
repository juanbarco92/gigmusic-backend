from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

''' -------------------- Modelos -------------------- '''

''' Base de Datos '''

# ----- Sub Modelos

class SongMetadata(BaseModel):

	artista: str
	cancion: str
	genero: str
	subgenero: str
	album: str
	año: str
	tonalidad: str
	capo: str

	def asDict(self):
		return {
			'artista' : self.artista,
			'cancion' : self.cancion,
			'genero' : self.genero,
			'subgenero' : self.subgenero,
			'album' : self.album,
			'año' : self.año,
			'tonalidad' : self.tonalidad,
			'capo' : self.capo
		}

class VerseContent(BaseModel):

	notas: str
	espacio: str
	letra: str

	def asDict(self):
		return {
			'notas' : self.notas,
			'espacio' : self.espacio,
			'letra' : self.letra,
		}

class SongVerse(BaseModel):

	tipo: str
	contenido: List[VerseContent]

	def asDict(self):
		return {
			'tipo' : self.tipo,
			'contenido' : self.contenido,
		}

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

class Song(BaseModel):

	metadata: SongMetadata
	canción: List[SongVerse]

	def asDict(self):
		return {
			'metadata' : self.metadata,
			'canción' : self.canción,
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

class SongEdition(BaseModel):

	metadata: Optional[SongMetadata] = None
	canción: Optional[List[SongVerse]] = None

	def asDict(self):
		return {
			'metadata' : self.metadata,
			'canción' : self.canción,
		}


# ----- Modelos de Seleccion

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
