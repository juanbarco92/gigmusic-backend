from typing import List
from fastapi import APIRouter, Depends
from dbs import mongo
from songs.models import Song, SongEdition
from utils.utils import classToDict
from security.authentication import auth_methods

db_m = mongo.data_base[1]
auth = Depends(auth_methods)

class SongView:
	
	router = APIRouter(
			prefix="/api/song",
		    tags=["song"]
			)

	''' Metodos para canciones '''

	@router.get("/", response_description='Obtiene una lista de canciones')
	async def read_song(busqueda: str, num_registros: int = 5):
		result = await mongo.find_many(busqueda, db_m, num_registros)
		return result

	@router.get("/one", response_description='Obtiene una cancion')
	async def read_one_song(id: str):
		result = await mongo.find_one(id, db_m)
		return result

	@router.post("/create_one", response_description='Añade una cancion')
	async def create_song(song: Song, username: str = auth):
		result = await mongo.insert_one(classToDict(song), db_m)
		return result

	@router.post("/create_many", response_description='Añade varias canciones')
	async def create_many_song(songs: List[Song], username: str = auth):
		result = await mongo.insert_many([classToDict(song) for song in songs], db_m)
		return result

	@router.patch("/edit/{song_id}", response_description='Edita una cancion, por favor elimine los campos no usados')
	async def update_song(song_id: str, song: SongEdition, username: str = auth):
		to_update = await mongo.find_one(song_id, db_m)
		if to_update is not None:
			update_data = song.dict(exclude_unset=True)
			update_model = SongEdition(**to_update).copy(update=update_data)
			result = await mongo.update_one(song_id, classToDict(update_model), db_m)
			return result
		return 'Invalid Id'

	@router.put("/replace/{song_id}", response_description='Reemplaza una cancion')
	async def replace_song(song_id: str, song: Song, username: str = auth):
		result = await mongo.replace_one(song_id, classToDict(song), db_m)
		return result

	@router.delete("/{song_id}", response_description='Elimina una cancion')
	async def delete_song(song_id: int, username: str = auth):
		result = await mongo.delete_one(song_id, db_m)
		return result
