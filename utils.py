from models import SongMetadata, SongVerse, VerseContent, ArtistSong

''' -------------------- Utilidades -------------------- '''

customClassTuple = (SongMetadata, SongVerse, VerseContent, ArtistSong)

# ----- Busqueda

def regexSearch(search):

	return {'$regex': f'^.*{search}.*$', '$options': 'i'}

# ----- Conversion de Modelos a Diccionarios

def classToDict(clase):
	principal = clase.asDict()
	list_helper = []
	for key in principal:
		if (isinstance(principal[key], customClassTuple)):
			sub = classToDict(principal[key])
			principal[key] = sub
		elif (isinstance(principal[key], list)):
			for i in principal[key]:
				print(i)
				if (isinstance(i, customClassTuple)):
					sub = classToDict(i)
					list_helper.append(sub)
			principal[key] = list_helper

	return principal
