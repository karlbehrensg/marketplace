import json
from fastapi import FastAPI

from src.domain import schemas
from src.adapters import publishers


app = FastAPI()


@app.get("/")
async def register_user(form: schemas.RegistrationForm):
    rpc_client = publishers.CommercesRpcClient()
    form_to_string = "message"
    response = rpc_client.call(form_to_string)
    return response
