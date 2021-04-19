from utils import regexSearch

def song_filter(search):
	regex_data = regexSearch(search)
	return {'$or': [
		{'metadata.cancion': regex_data}, 
		{'metadata.artista': regex_data},
		{'metadata.genero': regex_data},
		{'metadata.album': regex_data}
	]}