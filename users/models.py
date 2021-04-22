from typing import Optional
from pydantic import BaseModel

class User(BaseModel):

	username: str
	password: str
	email: str

class UserEdition(BaseModel):

	username: Optional[str]
	password: Optional[str]
	email: Optional[str]