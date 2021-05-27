import databases
import sqlalchemy
import pymysql

from utils.utils import MYSQL_HOST

pymysql.install_as_MySQLdb()

''' -------------------- Uso de MySQL -------------------- '''

#Inicializacion

db = databases.Database(MYSQL_HOST)

metadata = sqlalchemy.MetaData()

''' Tabla de Usuarios '''

users = sqlalchemy.Table(
	'users',
	metadata,
	sqlalchemy.Column('id', sqlalchemy.Integer, unique=True, primary_key=True),
	sqlalchemy.Column('username', sqlalchemy.String(50), unique=True),
	sqlalchemy.Column('nombre', sqlalchemy.String(100)),
	sqlalchemy.Column('password', sqlalchemy.String(200)),
	sqlalchemy.Column('email', sqlalchemy.String(50), unique=True),
	sqlalchemy.Column('is_admin', sqlalchemy.Boolean),
	sqlalchemy.Column('is_premium', sqlalchemy.Boolean),
	sqlalchemy.Column('is_eliminated', sqlalchemy.DateTime)
	)

''' Tabla de Analytics '''

analytics = sqlalchemy.Table(
	'analytics',
	metadata,
	sqlalchemy.Column('id', sqlalchemy.Integer, unique=True, primary_key=True),
	sqlalchemy.Column('user_id', sqlalchemy.Integer),
	sqlalchemy.Column('tipo', sqlalchemy.String(50)),
	sqlalchemy.Column('objeto', sqlalchemy.String(100)),
	sqlalchemy.Column('fecha', sqlalchemy.DateTime)
	)

# Creacion de tablas
engine = sqlalchemy.create_engine(
	MYSQL_HOST, 
	pool_recycle=3600
	)

metadata.create_all(engine)

''' Metodos de tabla users '''

# ===== Lectura
async def read_many():
	query = 'SELECT * FROM users'
	result = await db.fetch_all(query=query)
	return result

async def read_one(id: int):
	query = 'SELECT * FROM users WHERE id= :id'
	values={'id' : id}
	result = await db.fetch_one(query=query, values=values)
	return result

async def read_by_email(email: int):
	query = 'SELECT * FROM users WHERE email= :email'
	values={'email' : email}
	result = await db.fetch_one(query=query, values=values)
	return result

async def read_by_username(username: int):
	query = '''SELECT id, username, nombre, email, is_admin, is_premium 
		FROM users WHERE username= :username'''
	values={'username' : username}
	result = await db.fetch_one(query=query, values=values)
	return result

async def read_by_userauth(username: int):
	query = '''SELECT *	FROM users WHERE username= :username'''
	values={'username' : username}
	result = await db.fetch_one(query=query, values=values)
	return result

# ===== Escritura
async def create_one(user: dict):
	query = '''INSERT INTO users(username, nombre, password, email, is_admin, is_premium, is_eliminated) 
		VALUES (:username, :nombre, :password, :email, :is_admin, :is_premium, :is_eliminated)'''
	values = {
		'username' : user.username, 
		'nombre' : user.nombre, 
		'password' : user.password, 
		'email' : user.email, 
		'is_admin' : False,
		'is_premium' : False,
		'is_eliminated' : None
		}
	result = await db.execute(query=query, values=values)
	return result

# ===== Modificacion
async def replace_one(id: int, user: dict):
	query = '''UPDATE users SET username= :username, password= :password,
		email= :email WHERE id= :id'''
	values = {
		'username' : user.username, 
		'password' : user.password, 
		'email' : user.email,
		'id' : id 
		}
	result = await db.execute(query=query, values=values)
	return result

async def update_one(id: int, update: dict):
	query = '''UPDATE users SET username= :username, nombre= :nombre, password= :password,
		email= :email WHERE id= :id'''
	values = {
		'username' : update.username, 
		'nombre' : update.nombre, 
		'password' : update.password, 
		'email' : update.email,
		'id' : id 
		}
	result = await db.execute(query=query, values=values)
	return result

async def set_admin(id: int, is_admin: bool):
	query = '''UPDATE users SET is_admin= :is_admin WHERE id= :id'''
	values = {
		'is_admin' : is_admin, 
		'id' : id 
		}
	result = await db.execute(query=query, values=values)
	return result

async def set_premium(id: int, is_premium: bool):
	query = '''UPDATE users SET is_premium= :is_premium WHERE id= :id'''
	values = {
		'is_premium' : is_premium, 
		'id' : id 
		}
	result = await db.execute(query=query, values=values)
	return result

async def set_eliminated(id: int, is_eliminated:str):
	query = '''UPDATE users SET is_eliminated= :is_eliminated WHERE id= :id'''
	values = {
		'is_eliminated' : is_eliminated, 
		'id' : id 
		}
	result = await db.execute(query=query, values=values)
	return result

# ===== Eliminacion
async def delete_one(id: int):
	query = 'DELETE FROM users WHERE id= :id'
	values = {'id' : id}
	result = await db.execute(query=query, values=values)
	return result


''' Metodos de analytics '''

async def create_log(user_id: int, tipo: str, objeto: str, fecha: str):
	query = '''INSERT INTO analytics(user_id, tipo, objeto, fecha) 
	VALUES (:user_id, :tipo, :objeto, :fecha)'''
	values = {
		'user_id' : user_id,
		'tipo' : tipo,
		'objeto' : objeto,
		'fecha' : fecha
	}
	result = await db.execute(query=query, values=values)
	return result

async def read_log_by_id(user_id: int):
	query = 'SELECT * FROM analytics WHERE user_id = :user_id'
	values={'user_id' : user_id}
	result = await db.fetch_all(query=query, values=values)
	return result

async def count_log_obj(tipo: str, objeto: str):
	query = 'SELECT COUNT(id) FROM analytics WHERE objeto = :objeto AND tipo = :tipo'
	values={
		'objeto' : objeto,
		'tipo': tipo
	}
	result = await db.fetch_all(query=query, values=values)
	return result[0][0]

async def delete_log_by_date(fecha: str):
	query = 'DELETE FROM analytics WHERE fecha <= :fecha'
	values = {'fecha' : fecha}
	result = await db.execute(query=query, values=values)
	return result