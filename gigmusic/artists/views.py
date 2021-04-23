from typing import List
from fastapi import APIRouter, Depends
from dbs import mongo
from utils.utils import classToDict
from artists.models import Artist, ArtistEdition
from security.authentication import auth_methods

db_m = mongo.data_base[0]
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
			update_model = ArtistEdition(**to_update).copy(update=update_data)
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
