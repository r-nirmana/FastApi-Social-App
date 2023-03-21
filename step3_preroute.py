# from fastapi import FastAPI, Response, status, HTTPException, Depends
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional, List
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from sqlalchemy.orm import Session
# import time
# from . import models, schemas, utils
# from .database import engine, SessionLocal, get_db


# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()


# while True:    

#     try:
#         # environment variables to be added
#         conn = psycopg2.connect(host='localhost', database = 'fastapi', user = 'postgres', 
#         password = 'Adopado@77', cursor_factory=RealDictCursor)

#         cursor = conn.cursor()
#         print("Database Connection was succesfull")
#         break

#     except Exception as error:
#         print("Connection to databse failed !!")    
#         print("Error :", error)
#         time.sleep(2)

# #Path Operation or the Route

# @app.get("/")
# async def root():
#     return {"message": "Welcome to my api !!!!"}

# @app.get("/posts", response_model= List[schemas.PostResponse])
# def get_posts(db: Session = Depends(get_db)):
#     # cursor.execute(""" SELECT * FROM posts """)
#     # posts = cursor.fetchall()
#     # print(posts)
#     posts = db.query(models.posts).all()
#     return posts


# #creating a post    

# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

#     new_post = models.posts(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
    
#     return new_post

# # fetching an individual post from the id

# @app.get("/posts/{id}", response_model= schemas.PostResponse)
# def get_post(id: int, db:Session = Depends(get_db)):
#     # cursor.execute(""" SELECT * FROM posts WHERE id = %s """,(id,))
#     # post = cursor.fetchone()

#     post = db.query(models.posts).filter(models.posts.id == id).first()

#     if not post :
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with ID: {id} was not found")
#     return post

# # Deleting a single post

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db:Session = Depends(get_db)):
#     # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (id,))
#     # deleted_post = cursor.fetchone()
#     # conn.commit()

#     post_query = db.query(models.posts).filter(models.posts.id == id)

#     if post_query.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with ID : {id} does not exist")
    
#     post_query.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# # updating a post

# @app.put("/posts/{id}", response_model=schemas.PostResponse)
# def update_post(id:int, post: schemas.PostCreate, db:Session = Depends(get_db)):
#     # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
#     #                (post.title, post.content, post.published, (id,)) )
#     # updated_post = cursor.fetchone()
#     # conn.commit()
#     query_updated = db.query(models.posts).filter(models.posts.id == id)
    

#     if query_updated.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with ID : {id} does not exist")
    
#     # query_updated.update({'title':'updated title', 'content':'updated content'},synchronize_session=
#     #                      False)

#     query_updated.update(post.dict(),synchronize_session=False)
    

#     db.commit()
#     return query_updated.first()


# #.................................USERS..................................................
# #........................................................................................

# @app.post("/users", status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):

#     # hash the password - user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password

#     new_user = models.user(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# @app.get("/users/{id}", response_model=schemas.UserOut)
# def get_user(id:int, db:Session = Depends(get_db)):
#     user = db.query(models.user).filter(models.user.id == id).first()
#     if not user:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
#                             detail=f"user with id: {id} does not exist")
    
#     return user

