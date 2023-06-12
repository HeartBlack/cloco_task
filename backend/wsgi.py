from fastapi import FastAPI
from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware
from routers import userlogin, album, songs

app = FastAPI()
origins = ["http://localhost:3000"]

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
add_pagination(app)
app.include_router(
    userlogin.router,
    prefix="/api/v1",
    tags=["Sign up user and login"],
)
app.include_router(album.router, prefix="/api/v1/album", tags=["Album Crud"])
app.include_router(songs.router, prefix="/api/v1/songs", tags=["Songs Crud"])
