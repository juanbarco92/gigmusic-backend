from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from bson import ObjectId

from artist.utils import artist_filter
from song.utils import song_filter

import os

''' -------------------- Uso de MongoDB -------------------- '''

''' Inicializacion '''

load_dotenv()

client = AsyncIOMotorClient(os.getenv('MONGO_HOST'))
db = client.GIGMUSIC

# ===== Definicion de bases de datos

artistas = db.Artista
canciones = db.Canciones
data_base = ['artistas', 'canciones']
err = 'Error en seleccion de base de datos'

# ===== Conteo
async def count_search(field: str, search: str, bd: str):
	if bd == data_base[0]:
		count = await artistas.count_documents(artist_filter(search))
	elif bd == data_base[1]:
		count = await canciones.count_documents(song_filter(search))
	else:
		return err
	return count

# ===== Busqueda
async def find_one(id: str, bd: str):
	if bd == data_base[0]:
		result = await artistas.find_one({'_id': ObjectId(id)})
	elif bd == data_base[1]:
		result = await canciones.find_one({'_id': ObjectId(id)})
	else:
		return err
	if result is not None:
		result['id']=str(result.pop('_id'))
	else:
		return result
	return result

async def find_many(search: str, bd: str, length: int = 5):
	result = []
	if bd == data_base[0]:
		documents = await artistas.find(artist_filter(search)).to_list(length=length)
	elif bd == data_base[1]:
		documents = await canciones.find(song_filter(search)).to_list(length=length)
	else:
		return err
	if len(documents) > 0:
		for document in documents:
			document['id']=str(document.pop('_id'))
			result.append(document)
	return result

# ===== Adicion
async def insert_one(document: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.insert_one(document)
	elif bd == data_base[1]:
		result = await canciones.insert_one(document)
	else:
		return err
	return str(result.inserted_id)

async def insert_many(documents: list, bd: str):
	if bd == data_base[0]:
		result = await artistas.insert_many(documents)
	elif bd == data_base[1]:
		result = await canciones.insert_many(documents)
	else:
		return err
	return [str(res) for res in result.inserted_ids]

# ===== Modificacion
async def replace_one(id: str, document: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.replace_one({'_id': ObjectId(id)}, document)
	elif bd == data_base[1]:
		result = await canciones.replace_one({'_id': ObjectId(id)}, document)
	else:
		return err
	return result.modified_count

async def update_one(id: str, changes: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.update_one({'_id': ObjectId(id)}, { '$set': changes })
	elif bd == data_base[1]:
		result = await canciones.update_one({'_id': ObjectId(id)}, { '$set': changes })
	else:
		return err
	return result.modified_count

async def update_many(search: str, changes: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.update_many(artist_filter(search), { '$set': changes })
	elif bd == data_base[1]:
		result = await canciones.update_many(song_filter(search), { '$set': changes })
	else:
		return err
	return result.modified_count

# ===== Eliminacion
async def delete_one(id: str, bd: str):
	if bd == data_base[0]:
		result = await artistas.delete_one({'_id': ObjectId(id)})
	elif bd == data_base[1]:
		result = await canciones.delete_one({'_id': ObjectId(id)})
	else:
		return err
	return result.deleted_count

async def delete_many(field: str, search: str, bd: str):
	if bd == data_base[0]:
		result = await artistas.delete_many(artist_filter(search))
	elif bd == data_base[1]:
		result = await canciones.delete_many(song_filter(search))
	else:
		return err
	return result.delete_count
