from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import models,schemas
from ..database import get_db

router = APIRouter(
    prefix= "/posts"
)


# @router.get("/")
# async def root():
#     return {"message": "Welcome to my api !!!!"}

@router.get("/", response_model= List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.posts).all()
    return posts


#creating a post    

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = models.posts(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

# fetching an individual post from the id

@router.get("/{id}", response_model= schemas.PostResponse)
def get_post(id: int, db:Session = Depends(get_db)):
    post = db.query(models.posts).filter(models.posts.id == id).first()

    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with ID: {id} was not found")
    return post

# Deleting a single post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db:Session = Depends(get_db)):

    post_query = db.query(models.posts).filter(models.posts.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with ID : {id} does not exist")
    
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# updating a post

@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id:int, post: schemas.PostCreate, db:Session = Depends(get_db)):
    query_updated = db.query(models.posts).filter(models.posts.id == id)
    

    if query_updated.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with ID : {id} does not exist")

    query_updated.update(post.dict(),synchronize_session=False)
    

    db.commit()
    return query_updated.first()
