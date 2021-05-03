from typing import Optional
from pydantic import BaseModel

class UserNew(BaseModel):

	username: str
	nombre: str
	password: str
	verify_password: str
	email: str

class UserEdition(BaseModel):

	username: Optional[str]
	nombre: Optional[str]
	password: Optional[str]
	email: Optional[str]

class UserLogin(BaseModel):

	email: str
	password: str