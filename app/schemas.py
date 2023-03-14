from pydantic import BaseModel
from datetime import datetime

# class Post(BaseModel):
#     title : str
#     content : str
#     published : bool = True
#     #rating : Optional[int] = None


class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    #rating : Optional[int] = None

class PostCreate(PostBase):
    pass

# class PostResponse(BaseModel):
#     id: int
#     title : str
#     content : str
#     published : bool
#     created_at : datetime

#     class Config :
#         orm_mode = True

class PostResponse(PostBase):
    id: int
    created_at : datetime

    class Config :
        orm_mode = True