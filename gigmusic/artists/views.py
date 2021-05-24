from typing import List
from fastapi import APIRouter, Depends
from bson import ObjectId
from dbs import mongo
from utils.utils import classToDict
from artists.models import Artist, ArtistEdition, ArtistSong
from security.authentication import auth_methods

db_m = mongo.data_base[0]
db_s = mongo.data_base[1]
auth = Depends(auth_methods)

class ArtistView:

	router = APIRouter(
				prefix="/api/artist",
			    tags=["artist"]
				)

	''' Metodos para artistas '''

	@router.get("/", response_description='Obtiene una lista de artistas')
	async def read_artist(busqueda: str, num_registros: int = 5):
		result = await mongo.find_many(busqueda, db_m, num_registros)
		return result

	@router.get("/one", response_description='Obtiene un artista')
	async def read_one_artist(id: str):
		result = await mongo.find_one(id, db_m)
		return result

	@router.post("/create_one", response_description='Añade un artista')
	async def create_artist(artist: Artist, username: str = auth):
		result = await mongo.insert_one(classToDict(artist), db_m)
		return result

	@router.post("/create_many", response_description='Añade varios artistas')
	async def create_many_artist(artists: List[Artist], username: str = auth):
		result = await mongo.insert_many([classToDict(artist) for artist in artists], db_m)
		return result

	@router.patch("/edit/{artist_id}", response_description='Edita un artista, por favor elimine los campos no usados')
	async def update_artist(artist_id: str, artist: ArtistEdition, username: str = auth):
		to_update = await mongo.find_one(artist_id, db_m)
		if to_update is not None:
			update_data = artist.dict(exclude_unset=True)
			update_model = Artist(**to_update).copy(update=update_data)
			result = await mongo.update_one(artist_id, classToDict(update_model), db_m)
			return result
		return 'Invalid Id'

	@router.put("/replace/{artist_id}", response_description='Reemplaza un artista')
	async def replace_artist(artist_id: str, artist: Artist, username: str = auth):
		result = await mongo.replace_one(artist_id, classToDict(artist), db_m)
		return result

	@router.delete("/{artist_id}", response_description='Elimina un artista')
	async def delete_artist(artist_id: str, username: str = auth):
		result = await mongo.delete_one(artist_id, db_m)
		return result


	''' Metodos para el array de canciones'''

	@router.post("/create_one/{artist_id}/song", response_description='Adiciona una cancion a un artista')
	async def create_artist_song(artist_id: str, song: str, username: str = auth):
		to_update = await mongo.find_one(artist_id, db_m)
		update_model = Artist(**to_update)
		if to_update is not None:
			song_db = await mongo.find_many(update_model.nombre+' '+song, db_s)
			if song_db is not None:
				cancion = {
					'id': song_db[0]['id'],
					'cancion': song_db[0]['metadata']['cancion'],
					'album': song_db[0]['metadata']['album']
				}
				if update_model.canciones is not None:
					canciones_to_update = update_model.canciones
					canciones_to_update.append(ArtistSong(**cancion))
				else:
					canciones_to_update = []
					canciones_to_update.append(ArtistSong(**cancion))
				update_data = {'canciones': canciones_to_update}
				updated = update_model.copy(update=update_data)
				result = await mongo.update_one(artist_id, classToDict(updated), db_m)
				return result 
			return 'La canción no se encontró'
		return 'Invalid Id'

	@router.delete("/{artist_id}/song/{song_id}", response_description='Elimina una cancion de un artista')
	async def delete_artist_song(artist_id: str, song_id: str, username: str = auth):
		to_update = await mongo.find_one(artist_id, db_m)
		update_model = Artist(**to_update)
		if to_update is not None:
			if update_model.canciones is not None:
				cont=0
				canciones_to_update = []
				for c in update_model.canciones:
					if c.id != song_id:
						canciones_to_update.append(c)
						cont+=1
				if cont == len(update_model.canciones):
					return 'Invalid Id for Cancion'
				update_data = {'canciones': canciones_to_update}
				updated = update_model.copy(update=update_data)
				result = await mongo.update_one(artist_id, classToDict(updated), db_m)
				return result
			else:
				return 'Do not find Canciones'
		return 'Invalid Id for Artista'
