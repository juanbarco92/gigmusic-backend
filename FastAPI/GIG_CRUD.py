import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.college

class PyObjectId(ObjectId)
    @classmethod
    def __get_validators__(cls):
            yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class ArtistaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nombre: str = Field(...)
    genero: str = Field(...)
    subgenero: str
    decada: str = Field(...)
    canciones: list = Field(...)

@app.get(
    "/{nombre}", 
    response_description = "Obtiene un cantante con su discografia", 
    response_model=ArtistaModel
    )
def show_artist(name: str):
    if (artista := db["artistas"].find_one({"nombre": name})) is not NOne:
        return artista

        raise HTTPException(status_code=404, detail=f"Student {id} not found")
