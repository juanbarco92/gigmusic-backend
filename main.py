from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from models import Artist, Song, ArtistDB, SongDB
import mongo

''' -------------------- Main -------------------- '''

''' inicializacion '''
# uvicorn main:gigmusic --reload

gigmusic = FastAPI()

db = ['artistas', 'canciones']


''' Root '''
@gigmusic.get("/")
async def read_root():
	return {"GIGMUSIC": "FastAPI"}


''' Metodos para artistas '''

@gigmusic.get("/artist/{artist_id}")
async def read_artist(buscar: ArtistDB, busqueda: str):
	document = await mongo.find_many(buscar, busqueda, db[0])
	return document

@gigmusic.put("/artist/{artist_id}")
async def update_artist(buscar: ArtistDB, artist_id: int, artist: Artist):
	return 'por implementar'

@gigmusic.post("/artist/{artist_id}")
async def create_artist(buscar: ArtistDB, rtist: Artist):
	return 'por implementar'

@gigmusic.delete("/artist/{artist_id}")
async def delete_artist(buscar: ArtistDB, artist_id: int):
	return 'por implementar'


''' Metodos para canciones '''

@gigmusic.get("/song/{song_id}")
async def read_song(buscar: SongDB, busqueda: str):
	document = await mongo.find_many(buscar, busqueda, db[1])
	return document

@gigmusic.put("/song/{song_id}")
async def update_song(buscar: SongDB, song: Song):
	return 'por implementar'

@gigmusic.post("/song/{song_id}")
async def create_song(buscar: SongDB, song_id: int, song: Song):
	return 'por implementar'

@gigmusic.delete("/song/{song_id}")
async def delete_song(buscar: SongDB, song_id: int):
	return 'por implementar'
