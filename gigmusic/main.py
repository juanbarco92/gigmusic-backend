from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.utils import origins
from dbs import mysql

from users.views import UserView
from songs.views import SongView
from artists.views import ArtistView

''' -------------------- Main -------------------- '''

''' inicializacion '''
# uvicorn main:gigmusic --reload
# pip freeze > requirements.txt

gigmusic = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")
db_s = mysql.db

gigmusic.include_router(ArtistView.router)
gigmusic.include_router(SongView.router)
gigmusic.include_router(UserView.router)

gigmusic.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

''' Root '''
@gigmusic.on_event("startup")
async def startup():
    await db_s.connect()

@gigmusic.on_event("shutdown")
async def shutdown():
    await db_s.disconnect()

@gigmusic.get("/api")
async def read_root():
	return {"GIGMUSIC": "FastAPI"}
