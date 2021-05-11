from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

# ----- Hashed passwords
def verify_password(original_password, hashed_password):
    return pwd_context.verify(original_password, hashed_password)


def password_hash(password):
    return pwd_context.hash(password)

# ----- Busca valores en null de un diccionario y devuelve lista con las keys
def list_nulls(dic):
	lista = []
	for k,v in dic.items():
		if v == None:
			lista.append(k)
	return lista