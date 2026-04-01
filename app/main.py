
from fastapi import FastAPI

app = FastAPI(title="AI Knowledge API")


@app.get("/")
def home():
    return {"message": "Api running 🚀"}
