from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv

from utils import regexSearch

import os
import asyncio

''' -------------------- Uso de MongoDB -------------------- '''

''' Inicializacion '''

load_dotenv()

client = AsyncIOMotorClient(os.getenv('MONGO_HOST'))
db = client.GIG

MONGO_URL = os.getenv('MONGO_HOST')
client = AsyncIOMotorClient(MONGO_URL)
db = client.GIG

# ===== Definicion de bases de datos

artistas = db.artists_artistas
canciones = db.songs_canciones

# ===== Conteo
async def count_search(field: str, search: str, bd: str):
	if bd == 'artistas':
		count = await artistas.count_documents({field: regexSearch(search)}, {'_id':0})
	elif bd == 'canciones':
		count = await canciones.count_documents({f'metadata.{field}': regexSearch(search)}, {'_id':0})
	else:
		return 'Error en seleccion de base de datos'
	return count

# ===== Busqueda
async def find_one(field: str, search: str, bd: str):
	if bd == 'artistas':
		document = await artistas.find_one({field: regexSearch(search)}, {'_id':0})
	elif bd == 'canciones':
		document = await canciones.find_one({f'metadata.{field}': regexSearch(search)}, {'_id':0})
	else:
		return 'Error en seleccion de base de datos'
	return document

async def find_many(field: str, search: str, bd: str, length: int = 5):
	if bd == 'artistas':
		documents = await artistas.find({field: regexSearch(search)}, {'_id':0}).to_list(length=length)
	elif bd == 'canciones':
		documents = await canciones.find({f'metadata.{field}': regexSearch(search)}, {'_id':0}).to_list(length=length)
	else:
		return 'Error en seleccion de base de datos'
	return documents

# ===== Adicion
async def insert_one(document: dict, bd: str):
	if bd == 'artistas':
		result = await artistas.insert_one(document)
	elif bd == 'canciones':
		result = await canciones.insert_one(document)
	else:
		return 'Error en seleccion de base de datos'
	return result.inserted_id

async def insert_many(documents: list, bd: str):
	if bd == 'artistas':
		result = await artistas.insert_many(documents)
	elif bd == 'canciones':
		result = await canciones.insert_many(documents)
	else:
		return 'Error en seleccion de base de datos'
	return result.inserted_ids

# ===== Modificacion
async def replace_one(id: str, document: dict, bd: str):
	if bd == 'artistas':
		result = await artistas.replace_one({'_id': id}, document)
	elif bd == 'canciones':
		result = await canciones.replace_one({'_id': id}, document)
	else:
		return 'Error en seleccion de base de datos'
	return result.modified_count

async def update_one(id: str, changes: dict, bd: str):
	if bd == 'artistas':
		result = await artistas.update_one({'_id': id}, { '$set': changes })
	elif bd == 'canciones':
		result = await canciones.update_one({'_id': id}, { '$set': changes })
	else:
		return 'Error en seleccion de base de datos'
	return result.modified_count

async def update_many(field: str, search: str, changes: dict, bd: str):
	if bd == 'artistas':
		result = await artistas.update_many({field: regexSearch(search)}, { '$set': changes })
	elif bd == 'canciones':
		result = await canciones.update_many({f'metadata.{field}': regexSearch(search)}, { '$set': changes })
	else:
		return 'Error en seleccion de base de datos'
	return result.modified_count

# ===== Eliminacion
async def delete_one(id: str, bd: str):
	if bd == 'artistas':
		result = await artistas.delete_one({'_id': id})
	elif bd == 'canciones':
		result = await canciones.delete_one({'_id': id})
	else:
		return 'Error en seleccion de base de datos'
	return result.delete_count

async def delete_many(field: str, search: str, bd: str):
	if bd == 'artistas':
		result = await artistas.delete_many({field: regexSearch(search)})
	elif bd == 'canciones':
		result = await canciones.delete_many({f'metadata.{field}': regexSearch(search)})
	else:
		return 'Error en seleccion de base de datos'
	return result.delete_count
