from fastapi import APIRouter
from datetime import datetime
from dbs import mysql
from utils.utils import decode_token
from analytics.models import LogModel

class AnalyticView:

	router = APIRouter(
		prefix="/api/v1/analytic",
	    tags=["analytic"]
		)

	''' Metodos de Analytics'''

	@router.get('/', response_description='Lectura de registro de eventos')
	async def read_log(user_id: int):
		result = await mysql.read_log_by_id(user_id)
		return {'result': result}

	@router.get('/count', response_description='Conteo de eventos por objeto')
	async def count_log(tipo: str, objeto: str):
		result = await mysql.count_log_obj(tipo, objeto)
		return {'result': result}

	@router.post('/', response_description='Registro de eventos')
	async def write_log(data: LogModel):
		decoded = decode_token(data.token)
		fecha = datetime.now()
		user = await mysql.read_by_username(decoded['username'])
		result = await mysql.create_log(user.id, data.tipo, data.objeto, fecha)
		return {'result': result}

	@router.delete('/', response_description='Registro de eventos')
	async def delete_log(fecha: str):
		result = await mysql.delete_log_by_date(fecha)
		return {'result' : result}
		