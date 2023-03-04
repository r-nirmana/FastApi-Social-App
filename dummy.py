# from fastapi import FastAPI
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# #define a class how a post should look like

# class Post(BaseModel):
#     title : str
#     content : str
#     published : bool = True
#     rating : Optional[int] = None

# #Path Operation or the Route

# @app.get("/")
# async def root():
#     return {"message": "Welcome to my api !!!!"}

# @app.get("/posts")
# def get_posts():
#     return {"message": "These are your posts"}

# @app.post("/posts")
# def create_posts(new_post: Post):
#     print(new_post)
#     print(new_post.dict())
#     return{"Data": new_post}