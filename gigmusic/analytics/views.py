from fastapi import APIRouter
from datetime import datetime
from dbs import mysql
from utils.utils import decode_token, create_log
from analytics.models import LogModel

class AnalyticView:

	router = APIRouter(
		prefix="/api/analytic",
	    tags=["analytic"]
		)

	''' Metodos de Analytics'''

	@router.get('/', response_description='Lectura de registro de eventos')
	async def read_log(user_id: int):
		try:
			result = await mysql.read_log_by_id(user_id)
			return {'result': result}
		except:
			create_log()
			return {'error': 'Hubo un error de nuestra parte, lo sentimos'}

	@router.post('/', response_description='Registro de eventos')
	async def write_log(data: LogModel):
		try:
			decoded = decode_token(data.token)
			fecha = datetime.now()
			user = await mysql.read_by_username(decoded['username'])
			result = await mysql.create_log(user.id, data.tipo, data.objeto, fecha)
			return {'result': result}
		except:
			create_log()
			return {'error': 'Hubo un error de nuestra parte, lo sentimos'}

	@router.delete('/', response_description='Registro de eventos')
	async def delete_log(fecha: str):
		try:
			result = await mysql.delete_log_by_date(fecha)
			return {'result' : result}
		except:
			create_log()
			return {'error': 'Hubo un error de nuestra parte, lo sentimos'}
		