from typing import Optional
from pydantic import BaseModel

class UserNew(BaseModel):

	username: str
	nombre: str
	password: str
	verify_password: str
	email: str

class UserEdition(BaseModel):

	username: Optional[str] = None
	nombre: Optional[str] = None
	password: Optional[str] = None
	verify_password: Optional[str] = None
	email: Optional[str] = None
	password_ant: Optional[str] = None

class UserLogin(BaseModel):

	email: str
	password: str