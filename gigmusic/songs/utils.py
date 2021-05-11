from utils.utils import regexSearch

def song_filter(search):
	if (search.find(' ') > 0) : 
		busqueda = search.split(' ')
		l = []
		for buscar in busqueda:
			regex_data = regexSearch(buscar.strip())
			l.append(
				{'$or': [
					{'metadata.cancion': regex_data}, 
					{'metadata.artista': regex_data},
					{'metadata.genero': regex_data},
					{'metadata.album': regex_data}
				]}
			)
		return {'$and': l}
	else:
		buscar = search.strip()
		regex_data = regexSearch(buscar)
		return {'$or': [
					{'metadata.cancion': regex_data}, 
					{'metadata.artista': regex_data},
					{'metadata.genero': regex_data},
					{'metadata.album': regex_data}
				]}

