from fastapi import Depends

from database.dbConnect import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()