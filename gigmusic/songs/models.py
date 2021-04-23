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

class VerseContent(BaseModel):

	notas: str
	espacio: str
	letra: str

class SongVerse(BaseModel):

	tipo: str
	contenido: List[VerseContent]


# ----- Modelos Principales

class Song(BaseModel):

	metadata: SongMetadata
	canción: List[SongVerse]


# ----- Modelos de edicion

class SongEdition(BaseModel):

	metadata: Optional[SongMetadata] = None
	canción: Optional[List[SongVerse]] = None

