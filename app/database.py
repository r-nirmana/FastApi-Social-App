from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLACEHMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"

SQLACEHMY_DATABASE_URL = "postgresql://postgres:Adopado@77@localhost/fastapi"

engine = create_engine(SQLACEHMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
