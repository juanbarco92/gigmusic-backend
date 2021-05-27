from typing import List, Optional
from pydantic import BaseModel

''' -------------------- Modelos -------------------- '''

''' Base de Datos '''

# ----- Sub Modelos

class ArtistSong(BaseModel):

	id: str
	cancion: str
	album: str
	views: int


# ----- Modelos Principales

class Artist(BaseModel):

	nombre: str
	genero: str
	subgenero: str
	decada: str
	canciones: Optional[List[ArtistSong]] = []


# ----- Modelos de edicion

class ArtistEdition(BaseModel):

	nombre: Optional[str] = None
	genero: Optional[str] = None
	subgenero: Optional[str] = None
	decada: Optional[str] = None

