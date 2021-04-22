from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

from utils.utils import origins, SECURITY_TOKEN
from dbs import sqlite

from users.views import UserView
from songs.views import SongView
from artists.views import ArtistView

''' -------------------- Main -------------------- '''

''' inicializacion '''
# uvicorn main:gigmusic --reload
# pip freeze > requirements.txt

gigmusic = FastAPI()
db_s = sqlite.db

gigmusic.include_router(UserView.router)
gigmusic.include_router(SongView.router)
gigmusic.include_router(ArtistView.router)

gigmusic.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = OAuth2PasswordBearer(tokenUrl=SECURITY_TOKEN)

#token: str = Depends(security)
''' Root '''
@gigmusic.on_event("startup")
async def startup():
    await db_s.connect()

@gigmusic.on_event("shutdown")
async def shutdown():
    await db_s.disconnect()

@gigmusic.get("/api")
async def read_root(token: str = Depends(security)):
	return {"GIGMUSIC": "FastAPI"}
