from typing import List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bson import ObjectId

from models import Artist, Song, ArtistDB, SongDB, ArtistEdition, SongEdition
from utils import classToDict
import mongo

''' -------------------- Main -------------------- '''

''' inicializacion '''
# uvicorn main:gigmusic --reload

gigmusic = FastAPI()
db = mongo.data_base


''' Root '''
@gigmusic.get("/")
async def read_root():
	return {"GIGMUSIC": "FastAPI"}


''' Metodos para artistas '''

@gigmusic.get("/artist/{artist_id}", response_description='Obtiene una lista de artistas')
async def read_artist(buscar: ArtistDB, busqueda: str, num_registros: int = 5):
	result = await mongo.find_many(buscar, busqueda, db[0], num_registros)
	return result

@gigmusic.post("/artist/one", response_description='Añade un artista')
async def create_artist(artist: Artist):
	result = await mongo.insert_one(classToDict(artist), db[0])
	return result

@gigmusic.post("/artist/many", response_description='Añade varios artistas')
async def create_many_artist(artists: List[Artist]):
	result = await mongo.insert_many(artists, db[0])
	return result

@gigmusic.patch("/artist/edit/{artist_id}", response_description='Edita un artista, por favor elimine los campos no usados')
async def update_artist(artist_id: str, artist: ArtistEdition):
	to_update = await mongo.find_one(artist_id, db[0])
	update_data = artist.dict(exclude_unset=True)
	update_model = ArtistEdition(**to_update).copy(update=update_data)
	result = await mongo.update_one(artist_id, classToDict(update_model), db[0])
	return result

@gigmusic.put("/artist/replace/{artist_id}", response_description='Reemplaza un artista')
async def replace_artist(artist_id: str, artist: Artist):
	result = await mongo.replace_one(artist_id, classToDict(artist), db[0])
	return result

@gigmusic.delete("/artist/{artist_id}", response_description='Elimina un artista')
async def delete_artist(artist_id: str):
	result = await mongo.delete_one(artist_id, db[0])
	return result


''' Metodos para canciones '''

@gigmusic.get("/song/{song_id}", response_description='Obtiene una lista de canciones')
async def read_song(buscar: SongDB, busqueda: str, num_registros: int = 5):
	result = await mongo.find_many(buscar, busqueda, db[1], num_registros)
	return result

@gigmusic.post("/song/one", response_description='Añade una cancion')
async def create_song(song: Song):
	result = await mongo.insert_one(classToDict(song), db[1])
	return result

@gigmusic.post("/song/many", response_description='Añade varias canciones')
async def create_many_song(songs: List[Artist]):
	result = await mongo.insert_many(songs, db[1])
	return result

@gigmusic.patch("/song/edit/{song_id}", response_description='Edita una cancion, por favor elimine los campos no usados')
async def update_song(song_id: str, song: SongEdition):
	to_update = await mongo.find_one(song_id, db[0])
	update_data = song.dict(exclude_unset=True)
	update_model = SongEdition(**to_update).copy(update=update_data)
	result = await mongo.update_one(song_id, classToDict(update_model), db[1])
	return result

@gigmusic.put("/song/replace/{song_id}", response_description='Reemplaza una cancion')
async def replace_song(song_id: str, song: Song):
	result = await mongo.replace_one(song_id, classToDict(song), db[1])
	return result

@gigmusic.delete("/song/{song_id}", response_description='Elimina una cancion')
async def delete_song(song_id: int):
	result = await mongo.delete_one(song_id, db[1])
	return result
