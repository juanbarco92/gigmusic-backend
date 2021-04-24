from fastapi import APIRouter
from users.models import User, UserEdition
from dbs import mysql
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
		return result

	@router.get("/one", response_description='Obtiene un usuario')
	async def read_one_user(id: int):
		result = await mysql.read_one(id)
		return result

	@router.post("/", response_description='Añade un usuario')
	async def create_user(user: User):
		hash_pass = password_hash(user.password)
		user.password = hash_pass
		result = await mysql.create_one(user)
		return result

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
			return result
		return 'Invalid Id'

	@router.patch("/set_admin/{user_id}", response_description='Edita un usuario, por favor elimine los campos no usados')
	async def update_user_admin(user_id: int, is_admin: bool):
		to_update = await mysql.read_one(user_id)
		if to_update is not None:
			result = await mysql.set_admin(user_id, is_admin)
			return result
		return 'Invalid Id'

	@router.put("/replace/{user_id}", response_description='Reemplaza un usuario')
	async def replace_user(user_id: int, user: User):
		result = await mysql.replace_one(user_id, user)
		return result

	@router.delete("/{user_id}", response_description='Elimina un usuario')
	async def delete_user(user_id: int):
		result = await mysql.delete_one(user_id)
		return result
