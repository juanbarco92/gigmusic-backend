from typing import List
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bson import ObjectId

from song.models import Song, SongEdition
from artist.models import Artist, ArtistEdition
from users.models import User, UserEdition
from utils import classToDict, origins, SECURITY_TOKEN
import mongo
import sqlite

''' -------------------- Main -------------------- '''

''' inicializacion '''
# uvicorn main:gigmusic --reload
# pip freeze > requirements.txt

gigmusic = FastAPI()
db_m = mongo.data_base
db_s = sqlite.db

gigmusic.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#security = OAuth2PasswordBearer(tokenUrl=SECURITY_TOKEN)

#token: str = Depends(security)
''' Root '''
@gigmusic.on_event("startup")
async def startup():
    await db_s.connect()

@gigmusic.on_event("shutdown")
async def shutdown():
    await db_s.disconnect()

@gigmusic.get("/api")
async def read_root():
	return {"GIGMUSIC": "FastAPI"}


''' Metodos para artistas '''

@gigmusic.get("/api/artist", response_description='Obtiene una lista de artistas')
async def read_artist(busqueda: str, num_registros: int = 5):
	result = await mongo.find_many(busqueda, db_m[0], num_registros)
	return result

@gigmusic.get("/api/artist/one", response_description='Obtiene un artista')
async def read_one_artist(id: str):
	result = await mongo.find_one(id, db_m[0])
	return result

@gigmusic.post("/api/artist/one", response_description='Añade un artista')
async def create_artist(artist: Artist):
	result = await mongo.insert_one(classToDict(artist), db_m[0])
	return result

@gigmusic.post("/api/artist/many", response_description='Añade varios artistas')
async def create_many_artist(artists: List[Artist]):
	result = await mongo.insert_many([classToDict(artist) for artist in artists], db_m[0])
	return result

@gigmusic.patch("/api/artist/edit/{artist_id}", response_description='Edita un artista, por favor elimine los campos no usados')
async def update_artist(artist_id: str, artist: ArtistEdition):
	to_update = await mongo.find_one(artist_id, db_m[0])
	if to_update is not None:
		update_data = artist.dict(exclude_unset=True)
		update_model = ArtistEdition(**to_update).copy(update=update_data)
		result = await mongo.update_one(artist_id, classToDict(update_model), db_m[0])
		return result
	return 'Invalid Id'

@gigmusic.put("/api/artist/replace/{artist_id}", response_description='Reemplaza un artista')
async def replace_artist(artist_id: str, artist: Artist):
	result = await mongo.replace_one(artist_id, classToDict(artist), db_m[0])
	return result

@gigmusic.delete("/api/artist/{artist_id}", response_description='Elimina un artista')
async def delete_artist(artist_id: str):
	result = await mongo.delete_one(artist_id, db_m[0])
	return result


''' Metodos para canciones '''

@gigmusic.get("/api/song", response_description='Obtiene una lista de canciones')
async def read_song(busqueda: str, num_registros: int = 5):
	result = await mongo.find_many(busqueda, db_m[1], num_registros)
	return result

@gigmusic.get("/api/song/one", response_description='Obtiene una cancion')
async def read_one_song(id: str):
	result = await mongo.find_one(id, db_m[1])
	return result

@gigmusic.post("/api/song/one", response_description='Añade una cancion')
async def create_song(song: Song):
	result = await mongo.insert_one(classToDict(song), db_m[1])
	return result

@gigmusic.post("/api/song/many", response_description='Añade varias canciones')
async def create_many_song(songs: List[Song]):
	result = await mongo.insert_many([classToDict(song) for song in songs], db_m[1])
	return result

@gigmusic.patch("/api/song/edit/{song_id}", response_description='Edita una cancion, por favor elimine los campos no usados')
async def update_song(song_id: str, song: SongEdition):
	to_update = await mongo.find_one(song_id, db_m[0])
	if to_update is not None:
		update_data = song.dict(exclude_unset=True)
		update_model = SongEdition(**to_update).copy(update=update_data)
		result = await mongo.update_one(song_id, classToDict(update_model), db_m[1])
		return result
	return 'Invalid Id'

@gigmusic.put("/api/song/replace/{song_id}", response_description='Reemplaza una cancion')
async def replace_song(song_id: str, song: Song):
	result = await mongo.replace_one(song_id, classToDict(song), db_m[1])
	return result

@gigmusic.delete("/api/song/{song_id}", response_description='Elimina una cancion')
async def delete_song(song_id: int):
	result = await mongo.delete_one(song_id, db_m[1])
	return result


''' Metodos para usuarios '''

@gigmusic.get("/api/user", response_description='Obtiene una lista de usuarios')
async def read_user():
	result = await sqlite.read_many()
	return result

@gigmusic.get("/api/user/one", response_description='Obtiene un usuario')
async def read_one_user(user_id: int):
	result = await sqlite.read_one(user_id)
	return result

@gigmusic.post("/api/user", response_description='Añade un usuario')
async def create_user(user: User):
	result = await sqlite.create_one(user)
	return result

@gigmusic.patch("/api/user/edit/{user_id}", response_description='Edita un usuario, por favor elimine los campos no usados')
async def update_user(user_id: int, user: UserEdition):
	to_update = await sqlite.read_one(user_id)
	if to_update is not None:
		update_data = user.dict(exclude_unset=True)
		update_model = UserRegister(**to_update).copy(update=update_data)
		result = await sqlite.update_one(user_id, update_model)
		return result
	return 'Invalid Id'

@gigmusic.put("/api/user/replace/{user_id}", response_description='Reemplaza un usuario')
async def replace_user(user_id: int, user: User):
	result = await sqlite.replace_one(user_id, user)
	return result

@gigmusic.delete("/api/user/{user_id}", response_description='Elimina un usuario')
async def delete_user(user_id: int):
	result = await sqlite.delete_one(user_id)
	return result
