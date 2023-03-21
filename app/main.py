from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import time
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from .routers import post, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:    

    try:
        # environment variables to be added
        conn = psycopg2.connect(host='localhost', database = 'fastapi', user = 'postgres', 
        password = 'pwwwww', cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print("Database Connection was succesfull")
        break

    except Exception as error:
        print("Connection to databse failed !!")    
        print("Error :", error)
        time.sleep(2)

#Path Operation or the Route

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my api !!!!"}
