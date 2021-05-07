from utils.utils import regexSearch

def artist_filter(search):
	if (search.find(' ') > 0) : 
		busqueda = search.split(' ')
		l = []
		for buscar in busqueda:
			regex_data = regexSearch(buscar.strip())
			l.append(
				{'$or': [
						{'nombre': regex_data}, 
						{'genero': regex_data}
				]}
			)
		return {'$and': l}
	else:
		buscar = search.strip()
		regex_data = regexSearch(buscar)
		return {'$or': [
					{'nombre': regex_data}, 
					{'genero': regex_data}
				]}
