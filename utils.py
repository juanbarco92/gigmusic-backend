
''' -------------------- Utilidades -------------------- '''

def regexSearch(search):
	return {'$regex': f'^.*{search}.*$', '$options': 'i'}
