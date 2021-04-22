from typing import Optional
from pydantic import BaseModel

class User(BaseModel):

	id: int
	username: str
	password: str
	email: str
	is_admin: bool

class UserEdition(BaseModel):

	username: Optional[str]
	password: Optional[str]
	email: Optional[str]