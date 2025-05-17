from fastapi import APIRouter, Request
import os

from database.models import User
from database.dbConnect import SessionLocal

router = APIRouter()
db = SessionLocal()



