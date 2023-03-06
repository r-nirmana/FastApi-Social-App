from .database import Base
from sqlalchemy import column, Integer, String, Boolean

class posts(Base):
    __tablename__= "posts"

    id = column(Integer, primary_key=True, nullable= False)
    title =column(String, nullable= False)
    content = column(String, nullable=False)    
    published = column(Boolean, default=True)