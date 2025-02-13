from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

DB_URL = "postgresql+psycopg2://postgres:27945501dias@localhost:5432/workermanager"

engine = create_engine(
    url=DB_URL,
    echo=False,
)
session_factory = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass