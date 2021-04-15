from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from models import Artist, Song, ArtistDB, SongDB
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

@gigmusic.get("/artist/{artist_id}")
async def read_artist(buscar: ArtistDB, busqueda: str):
	document = await mongo.find_many(buscar, busqueda, db[0])
	return document

@gigmusic.post("/artist/{artist_id}")
async def create_artist(artist: Artist):
	result = await mongo.insert_one(artist.asdict(), db[0])
	return result

@gigmusic.put("/artist/{artist_id}")
async def update_artist(artist_id: str, artist: Artist):
	result = await mongo.update_one(artist_id, artist.asdict(), db[0])
	return result

@gigmusic.delete("/artist/{artist_id}")
async def delete_artist(artist_id: str):
	return 'por implementar'


''' Metodos para canciones '''

@gigmusic.get("/song/{song_id}")
async def read_song(buscar: SongDB, busqueda: str):
	document = await mongo.find_many(buscar, busqueda, db[1])
	return document

@gigmusic.post("/song/{song_id}")
async def create_song(song: Song):
	return 'por implementar'

@gigmusic.put("/song/{song_id}")
async def update_song(song_id: str, song: Song):
	return 'por implementar'

@gigmusic.delete("/song/{song_id}")
async def delete_song(song_id: int):
	return 'por implementar'
