from pydantic import BaseModel

class LogModel(BaseModel):

	token: str
	tipo: str
	objeto: str