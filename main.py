from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

#define a class how a post should look like

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    #rating : Optional[int] = None

while True:    

    try:
        # environment variables to be added
        conn = psycopg2.connect(host='localhost', database = 'fastapi', user = 'postgres', 
        password = 'password', cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print("Database Connection was succesfull")
        break

    except Exception as error:
        print("Connection to databse failed !!")    
        print("Error :", error)
        time.sleep(2)

#Path Operation or the Route

@app.get("/")
async def root():
    return {"message": "Welcome to my api !!!!"}

@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    return {"Data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    #print(new_post)
    #print(new_post.dict())
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)
      RETURNING * """, (post.title, post.content, post.published))
    
    new_post = cursor.fetchone()
    conn.commit()
    print(new_post)

    return{"Data": new_post}

# fetching an individual post from the id

@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """,(id,))
    post = cursor.fetchone()

    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with ID: {id} was not found")
    return{"post_detail": post}

# Deleting a single post

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (id,))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with ID : {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
