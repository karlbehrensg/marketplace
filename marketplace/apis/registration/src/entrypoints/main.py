from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def register_user():
    return {"message": "Hello World!"}
