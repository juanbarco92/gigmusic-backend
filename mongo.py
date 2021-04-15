from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from bson import ObjectId

from utils import regexSearch

import os
import asyncio

''' -------------------- Uso de MongoDB -------------------- '''

''' Inicializacion '''

load_dotenv()

client = AsyncIOMotorClient(os.getenv('MONGO_HOST'))
db = client.GIG

# ===== Definicion de bases de datos

artistas = db.artists_artistas
canciones = db.songs_canciones
data_base = ['artistas', 'canciones']

# ===== Conteo
async def count_search(field: str, search: str, bd: str):
	if bd == data_base[0]:
		count = await artistas.count_documents({field: regexSearch(search)})
	elif bd == data_base[1]:
		count = await canciones.count_documents({f'metadata.{field}': regexSearch(search)})
	else:
		return 'Error en seleccion de base de datos'
	return count

# ===== Busqueda
async def find_one(field: str, search: str, bd: str):
	if bd == data_base[0]:
		document = await artistas.find_one({field: regexSearch(search)}, {'_id':0})
	elif bd == data_base[1]:
		document = await canciones.find_one({f'metadata.{field}': regexSearch(search)}, {'_id':0})
	else:
		return 'Error en seleccion de base de datos'
	return document

async def find_many(field: str, search: str, bd: str, length: int = 5):
	if bd == data_base[0]:
		documents = await artistas.find({field: regexSearch(search)}, {'_id':0}).to_list(length=length)
	elif bd == data_base[1]:
		documents = await canciones.find({f'metadata.{field}': regexSearch(search)}, {'_id':0}).to_list(length=length)
	else:
		return 'Error en seleccion de base de datos'
	return documents

# ===== Adicion
async def insert_one(document: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.insert_one(document)
	elif bd == data_base[1]:
		result = await canciones.insert_one(document)
	else:
		return 'Error en seleccion de base de datos'
	return str(result.inserted_id)

async def insert_many(documents: list, bd: str):
	if bd == data_base[0]:
		result = await artistas.insert_many(documents)
	elif bd == data_base[1]:
		result = await canciones.insert_many(documents)
	else:
		return 'Error en seleccion de base de datos'
	return result.inserted_ids

# ===== Modificacion
async def replace_one(id: str, document: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.replace_one({'_id': ObjectId(id)}, document)
	elif bd == data_base[1]:
		result = await canciones.replace_one({'_id': ObjectId(id)}, document)
	else:
		return 'Error en seleccion de base de datos'
	return result.modified_count

async def update_one(id: str, changes: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.update_one({'_id': ObjectId(id)}, { '$set': changes })
	elif bd == data_base[1]:
		result = await canciones.update_one({'_id': ObjectId(id)}, { '$set': changes })
	else:
		return 'Error en seleccion de base de datos'
	return result.modified_count

async def update_many(field: str, search: str, changes: dict, bd: str):
	if bd == data_base[0]:
		result = await artistas.update_many({field: regexSearch(search)}, { '$set': changes })
	elif bd == data_base[1]:
		result = await canciones.update_many({f'metadata.{field}': regexSearch(search)}, { '$set': changes })
	else:
		return 'Error en seleccion de base de datos'
	return result.modified_count

# ===== Eliminacion
async def delete_one(id: str, bd: str):
	if bd == data_base[0]:
		result = await artistas.delete_one({'_id': ObjectId(id)})
	elif bd == data_base[1]:
		result = await canciones.delete_one({'_id': ObjectId(id)})
	else:
		return 'Error en seleccion de base de datos'
	return result.deleted_count

async def delete_many(field: str, search: str, bd: str):
	if bd == data_base[0]:
		result = await artistas.delete_many({field: regexSearch(search)})
	elif bd == data_base[1]:
		result = await canciones.delete_many({f'metadata.{field}': regexSearch(search)})
	else:
		return 'Error en seleccion de base de datos'
	return result.delete_count
