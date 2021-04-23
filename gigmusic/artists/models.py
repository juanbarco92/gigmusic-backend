from typing import List, Optional
from pydantic import BaseModel

''' -------------------- Modelos -------------------- '''

''' Base de Datos '''

# ----- Sub Modelos

class ArtistSong(BaseModel):

	cancion: str


# ----- Modelos Principales

class Artist(BaseModel):

	nombre: str
	genero: str
	subgenero: str
	decada: str
	canciones: List[ArtistSong]


# ----- Modelos de edicion

class ArtistEdition(BaseModel):

	nombre: Optional[str] = None
	genero: Optional[str] = None
	subgenero: Optional[str] = None
	decada: Optional[str] = None
	canciones: Optional[List[ArtistSong]] = None

