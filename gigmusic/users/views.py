from fastapi import APIRouter
from datetime import datetime

from dbs import mysql
from utils.utils import create_token, str_to_json
from users.models import UserNew, UserEdition, UserLogin
from users.utils import password_hash, verify_password

class UserView:

	router = APIRouter(
		prefix="/api/user",
	    tags=["user"]
		)

	''' Metodos para usuarios '''

	@router.get("/", response_description='Obtiene una lista de usuarios')
	async def read_user():
		result = await mysql.read_many()
		return {'result': result, 'error': None}

	@router.get("/one", response_description='Obtiene un usuario')
	async def read_one_user(id: int):
		result = await mysql.read_one(id)
		return {'result': result, 'error': None}

	@router.post("/", response_description='Añade un usuario')
	async def create_user(user: UserNew):
		data = await mysql.read_by_email(user.email)
		dato = await mysql.read_by_username(user.username)
		if data is None:
			if dato is None:
				if user.password == user.verify_password:
					hash_pass = password_hash(user.password)
					user.password = hash_pass
					result = await mysql.create_one(user)
					return {'result': result, 'error': None}
				return {'error': 'Las contraseñas no coinciden'}
			return {'error': 'El nombre de usuario ya esta en uso'}
		return {'error': 'El correo ya se encuentra registrado'}

	@router.patch("/edit/{user_id}", response_description='Edita un usuario, por favor elimine los campos no usados')
	async def update_user(user_id: int, user: UserEdition):
		to_update = await mysql.read_one(user_id)
		if to_update is not None:
			update_data = user.dict(exclude_unset=True)
			update_model = UserEdition(**to_update).copy(update=update_data)
			try:
				if update_data['password']:
					hash_pass = password_hash(update_model.password)
					update_model.password = hash_pass
			except:
				pass
			result = await mysql.update_one(user_id, update_model)
			return {'result': result, 'error': None}
		return {'error': 'Invalid Id'}

	@router.patch("/set_admin/{user_id}", response_description='Edita un usuario, por favor elimine los campos no usados')
	async def update_user_admin(user_id: int, is_admin: bool):
		to_update = await mysql.read_one(user_id)
		if to_update is not None:
			result = await mysql.set_admin(user_id, is_admin)
			return {'result': result, 'error': None}
		return {'error': 'Invalid Id'}

	@router.patch("/set_premium/{user_id}", response_description='Edita un usuario, por favor elimine los campos no usados')
	async def update_user_premium(user_id: int, is_premium: bool):
		to_update = await mysql.read_one(user_id)
		if to_update is not None:
			result = await mysql.set_premium(user_id, is_premium)
			return {'result': result, 'error': None}
		return {'error': 'Invalid Id'}

	@router.patch("/set_eliminated/{user_id}", response_description='Edita un usuario, por favor elimine los campos no usados')
	async def update_user_eliminated(user_id: int, is_eliminated: bool):
		to_update = await mysql.read_one(user_id)
		if to_update is not None:
			if(is_eliminated==True):
				eliminated = datetime.now()
			elif(is_eliminated==False):
				eliminated = None
			else:
				return {'error': 'Error occurred, no boolean value for is_eliminated'}
			result = await mysql.set_eliminated(user_id, eliminated)
			return result
		return {'error': 'Invalid Id'}

	@router.put("/replace/{user_id}", response_description='Reemplaza un usuario')
	async def replace_user(user_id: int, user: UserNew):
		result = await mysql.replace_one(user_id, user)
		return {'result': result, 'error': None}

	@router.delete("/{user_id}", response_description='Elimina un usuario')
	async def delete_user(user_id: int):
		result = await mysql.delete_one(user_id)
		return {'result': result, 'error': None}


	''' Metodos de Login '''

	@router.post("/login", response_description='Obtiene un token')
	async def login_token(credentials: UserLogin):
		data = await mysql.read_by_email(credentials.email)
		if data is not None:
			if data.is_eliminated is None:
				if verify_password(credentials.password, data.password):
					token = create_token({'email' : data.email, 'username' : data.username})
					return {'token': token, 'error': None}
				return {'error': 'Usuario o contraseña equivocados'}
			return {'error': 'La cuenta se encuentra desactivada'}
		return {'error': 'El email no se encuentra registrado'}
