from fastapi import FastAPI, Depends
from app.core.config import settings
from sqlalchemy.orm import Session
from app.db.pgsql_database import get_db

app = FastAPI()

@app.get("/")
def Hello_World():
    return {"message": "Hello World!"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"health":"ok"}