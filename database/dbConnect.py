from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base

load_dotenv()

DB_URL = os.getenv("DB_URL")
if DB_URL is None:
	raise ValueError("Environment variable 'DB_URL' is not set.")

engine = create_engine(url=DB_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def create_tables():
    print("Creating Tables...")
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Failed to create tables: {e}")

