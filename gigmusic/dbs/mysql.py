import databases
import sqlalchemy
import pymysql

from utils.utils import MYSQL_HOST

pymysql.install_as_MySQLdb()

''' -------------------- Uso de SQLite -------------------- '''

''' Inicializacion '''

db = databases.Database(MYSQL_HOST)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
	'users',
	metadata,
	sqlalchemy.Column('id', sqlalchemy.Integer, unique=True),
	sqlalchemy.Column('username', sqlalchemy.String(50), unique=True),
	sqlalchemy.Column('nombre', sqlalchemy.String(100)),
	sqlalchemy.Column('password', sqlalchemy.String(200)),
	sqlalchemy.Column('email', sqlalchemy.String(50), primary_key=True, unique=True),
	sqlalchemy.Column('is_admin', sqlalchemy.Boolean),
	sqlalchemy.Column('is_premium', sqlalchemy.Boolean),
	sqlalchemy.Column('is_eliminated', sqlalchemy.DateTime)
	)
# Crea las tablas de datos
engine = sqlalchemy.create_engine(
	MYSQL_HOST, 
	pool_recycle=3600
	)

metadata.create_all(engine)

# ===== Lectura
async def read_many():
	query = 'SELECT * FROM users'
	result = await db.fetch_all(query=query)
	return result

async def read_one(id: int):
	query = 'SELECT * FROM users WHERE id= :id'
	result = await db.fetch_one(query=query, values={'id' : id})
	return result

async def read_by_email(email: int):
	query = 'SELECT * FROM users WHERE email= :email'
	result = await db.fetch_one(query=query, values={'email' : email})
	return result

async def read_by_username(username: int):
	query = '''SELECT id, username, nombre, email, is_admin, is_premium 
		FROM users WHERE username= :username'''
	result = await db.fetch_one(query=query, values={'username' : username})
	return result

async def read_by_userauth(username: int):
	query = '''SELECT *	FROM users WHERE username= :username'''
	result = await db.fetch_one(query=query, values={'username' : username})
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