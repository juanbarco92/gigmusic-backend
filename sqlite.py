import databases
import sqlalchemy

from utils import SQL_HOST

''' -------------------- Uso de SQLite -------------------- '''

''' Inicializacion '''

db = databases.Database(SQL_HOST)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
	'users',
	metadata,
	sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
	sqlalchemy.Column('username', sqlalchemy.String, unique=True),
	sqlalchemy.Column('password', sqlalchemy.String),
	sqlalchemy.Column('email', sqlalchemy.String, unique=True),
	sqlalchemy.Column('is_admin', sqlalchemy.Boolean)
	)
# Crea las tablas de datos
engine = sqlalchemy.create_engine(
	SQL_HOST, 
	connect_args={"check_same_thread": False}
	)

metadata.create_all(engine)

# ===== Lectura
async def read_many():
	query = 'SELECT * FROM users'
	result = await db.fetch_all(query=query)
	return result

async def read_one(user_id: int):
	query = 'SELECT * FROM users WHERE id= :id'
	result = await db.fetch_one(query=query, values={'id' : user_id})
	return result

# ===== Escritura
async def create_one(user: dict):
	query = '''INSERT INTO users(username, password, email, is_admin) 
		VALUES (:username, :password, :email, :is_admin)'''
	values = {
		'username' : user.username, 
		'password' : user.password, 
		'email' : user.email, 
		'is_admin' : False
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
	query = '''UPDATE users SET username= :username, password= :password,
		email= :email WHERE id= :id'''
	values = {
		'username' : update.username, 
		'password' : update.password, 
		'email' : update.email,
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