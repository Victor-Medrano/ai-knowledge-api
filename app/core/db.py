
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ai_knowledge.db")

engine_kargs = {}
if DATABASE_URL.startswith("sqlite"):
    engine_kargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, echo=True, future=True, **engine_kargs)

SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, class_=Session)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
