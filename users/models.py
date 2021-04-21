from pydantic import BaseModel

class User(BaseModel):

	id: int
	username: str
	password: str
	email: str
	is_admin: bool

	def asDict(self):
		return {
			'id' : self.id,
			'username' : self.username,
			'password' : self.password,
			'email' : self.email,
			'is_admin' : self.is_admin
		}

class UserRegister(BaseModel):

	username: str
	password: str
	email: str

	def asDict(self):
		return {
			'username' : self.username,
			'password' : self.password,
			'email' : self.email
		}