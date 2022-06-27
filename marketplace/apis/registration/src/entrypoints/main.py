from fastapi import FastAPI

from src.domain import schemas


app = FastAPI()


@app.get("/")
async def register_user(form: schemas.RegistrationForm):
    return {"message": "Hello World!"}
