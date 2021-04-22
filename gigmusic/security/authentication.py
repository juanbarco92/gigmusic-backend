from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from dbs import sqlite
import secrets

security = HTTPBasic()

async def auth_methods(credentials: HTTPBasicCredentials = Depends(security)):
    userindb = await sqlite.read_one(credentials.username)
    correct_password = secrets.compare_digest(credentials.password, userindb.password)
    if not (correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email y/o contraseña incorrectos",
            headers={"WWW-Authenticate": "Basic"},
        )
    elif not (userindb.is_admin):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No tiene permisos para esta acción",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username