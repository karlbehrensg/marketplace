from fastapi import FastAPI, Depends

from src.domain import schemas
from src.adapters.publishers import PublisherClient, CommercesRpcClient


app = FastAPI()


@app.get("/")
async def register_user(
    form: schemas.RegistrationForm, 
    rpc_client: PublisherClient = Depends(CommercesRpcClient)
):
    form_to_string = "message"
    response = rpc_client.call(form_to_string)
    return response
