import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# DATABASE_URL = os.getenv("PGSQL_DATABASE_URL","")
print(f"CURRENT SETTINGS -> ENV: '{settings.ENV}', DEBUG: {settings.DEBUG}")

if settings.ENV == 'development' and settings.DEBUG:
    print("connection url db : ", settings.PGSQL_DATABASE_URL)

engine = create_engine(
    settings.PGSQL_DATABASE_URL, 
    pool_pre_ping=True,     
    pool_size=10, 
    max_overflow=20)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()