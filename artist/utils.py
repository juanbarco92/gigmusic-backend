from utils import regexSearch

def artist_filter(search):
	regex_data = regexSearch(search)
	return {'$or': [
		{'nombre': regex_data}, 
		{'genero': regex_data}
	]}