from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from users.utils import verify_password
from dbs import mysql

security = HTTPBasic()

async def auth_methods(credentials: HTTPBasicCredentials = Depends(security)):
    userindb = await mysql.read_by_user(credentials.username)
    correct_password = verify_password(credentials.password, userindb.password)
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