
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.core.db import get_db

load_dotenv()


app = FastAPI(title="AI Knowledge API")


@app.get("/")
def home():
    return {"message": "Api running 🚀"}


@app.get("/test_bd")
def testing_db(db: Session = Depends(get_db)):
    return {"message": "Conected"}
