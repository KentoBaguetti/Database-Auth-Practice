from fastapi import FastAPI
from dotenv import load_dotenv
import os

from routes.routes import router as Routes
from database.dbConnect import engine, create_tables

load_dotenv()

app = FastAPI()

app.include_router(Routes, prefix="/api")

@app.on_event("startup")
async def startup():
    try:
        with engine.connect() as connection:
            print("Connected to DB")
            create_tables()
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        
@app.on_event("shutdown")
async def shutdown():
    print("Shutting down DB")

@app.get("/")
def root():
    return {
        "message" : "Success"
    }