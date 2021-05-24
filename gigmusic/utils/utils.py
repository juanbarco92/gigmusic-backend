from dotenv import load_dotenv
from songs.models import SongMetadata, SongVerse, VerseContent
from artists.models import ArtistSong
import os
import json
import jwt

load_dotenv()
''' -------------------- Utilidades -------------------- '''

# ----- Variables ENV

MONGO_HOST = os.getenv('MONGO_HOST')
MYSQL_HOST = os.getenv('MYSQL_HOST')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

# ----- Origenes de CORS

origins = [
    "localhost:3000",
    "localhost"
]

# ----- Clases personalizadas
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
				else:
					list_helper.append(i)
			principal[key] = list_helper

	return principal

# ----- Create JWT Token
def create_token(data):
	encoded = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
	return encoded

# ----- Decode JWT Token
def decode_token(token):
	decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
	return decoded

# ----- Cambio de string a JSON
def str_to_json(data):
	return json.loads(data)