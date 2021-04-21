from typing import List, Optional
from pydantic import BaseModel

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


# ----- Modelos Principales

class Song(BaseModel):

	metadata: SongMetadata
	canción: List[SongVerse]

	def asDict(self):
		return {
			'metadata' : self.metadata,
			'canción' : self.canción,
		}


# ----- Modelos de edicion

class SongEdition(BaseModel):

	metadata: Optional[SongMetadata] = None
	canción: Optional[List[SongVerse]] = None

	def asDict(self):
		return {
			'metadata' : self.metadata,
			'canción' : self.canción,
		}
