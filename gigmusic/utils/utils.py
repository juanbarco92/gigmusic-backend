from dotenv import load_dotenv
from songs.models import SongMetadata, SongVerse, VerseContent
from artists.models import ArtistSong
import os

load_dotenv()
''' -------------------- Utilidades -------------------- '''

# ----- Variables ENV

MONGO_HOST = os.getenv('MONGO_HOST')
SQL_HOST = os.getenv('SQL_HOST')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

origins = [
    ".*localhost:3000/.*",
    "127.0.0.1:.*",
    "*"
]

customClassTuple = (SongMetadata, SongVerse, VerseContent, ArtistSong)

# ----- Busqueda

def regexSearch(search):
	s=''
	for l in search.lower():
		if l=='a' or l=='á':
			s+='[aá]'
		elif l=='e' or l=='é':
			s+='[eé]'
		elif l=='i' or l=='í':
			s+='[ií]'
		elif l=='o' or l=='ó':
			s+='[oó]'
		elif l=='u' or l=='ú' or l=='ü':
			s+='[uúü]'
		else:
			s+=l
	return {'$regex': f'^.*{s}.*$', '$options': 'i'}

# ----- Conversion de Modelos a Diccionarios

def classToDict(clase):
	principal = clase.dict()
	list_helper = []
	for key in principal:
		if (isinstance(principal[key], customClassTuple)):
			sub = classToDict(principal[key])
			principal[key] = sub
		elif (isinstance(principal[key], list)):
			for i in principal[key]:
				if (isinstance(i, customClassTuple)):
					sub = classToDict(i)
					list_helper.append(sub)
			principal[key] = list_helper

	return principal
