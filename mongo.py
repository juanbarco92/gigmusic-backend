from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv

from utils import regexSearch

import os
import asyncio

''' -------------------- Uso de MongoDB -------------------- '''

load_dotenv()

client = AsyncIOMotorClient(os.getenv('MONGO_HOST'))
db = client.GIG

MONGO_URL = os.getenv('MONGO_HOST')
client = AsyncIOMotorClient(MONGO_URL)
db = client.GIG

''' Coleccion artistas '''

async def artist_find_one():
	document = await db.artists_artistas.find_one({'nombre': regexSearch(q)}, {'_id':0})
	return document

async def artist_find_many(q: str, length: int = 5):
	document = await db.artists_artistas.find({'nombre': regexSearch(q)}, {'_id':0}).to_list(length=length)
	return document

''' Coleccion canciones'''

async def song_find_one():
	document = await db.songs_canciones.find_one({ 'metadata.cancion': regexSearch(q)}, {'_id':0})
	return document

async def song_find_many(q:str, length: int = 5):
	document = await db.songs_canciones.find({'metadata.cancion': regexSearch(q)}, {'_id':0}).to_list(length=length)
	return document