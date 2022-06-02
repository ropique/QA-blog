from unicodedata import category
from fastapi import FastAPI
from pydantic import BaseModel, BaseSettings
from fastapi.middleware.cors import CORSMiddleware
from app.routers import posts, user, auth, vote
from .database import engine,  get_db, SessionLocal
from sqlalchemy.orm import Session 
from . import models, schemas, utils




app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "QA engineering fastapi: In 'docs' you can see Documentation"}

