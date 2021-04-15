from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from models import Artist, Song
import mongo

''' -------------------- Main -------------------- '''

# uvicorn main:app --reload

app = FastAPI()

''' Root '''
@app.get("/")
async def read_root():
	return {"GIGMUSIC": "FastAPI"}

''' Metodos para artistas '''

@app.get("/artist/{artist_id}")
async def read_artist(nombre: str):
	document = await mongo.artist_find_many(nombre)
	return document

@app.put("/artist/{artist_id}")
async def update_artist(artist_id: int, artist: Artist):
	return {"artist_nombre": artist.nombre, "artist_id": artist_id}

@app.post("/artist/{artist_id}")
async def create_artist(artist: Artist):
	return {"artist_nombre": artist.nombre}

@app.delete("/artist/{artist_id}")
async def delete_artist(artist_id: int):
	return {"artist_id": artist_id}

''' Metodos para canciones '''

@app.get("/song/{song_id}")
async def read_song(cancion: str):
	document = await mongo.song_find_many(cancion)
	return document

@app.put("/song/{song_id}")
async def update_song(song: Song):
	return {"song_nombre": song.nombre}

@app.post("/song/{song_id}")
async def create_song(song_id: int, song: Song):
	return {"song_nombre": song.nombre, "song_id": song_id}

@app.delete("/song/{song_id}")
async def delete_song(song_id: int):
	return {"song_id": song_id}