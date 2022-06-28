import json
from fastapi import FastAPI, Depends

from src.domain import schemas, models
from src.adapters.publishers import PublisherClient, CommercesRpcClient


app = FastAPI()


@app.get("/")
async def register_user(
    form: schemas.RegistrationForm, 
    rpc_client: PublisherClient = Depends(CommercesRpcClient)
):
    commerce = models.Commerce(form.legal_id, form.name, form.email, form.retail_name)
    body = {
        "cmd": "create",
        "data": commerce.__dict__
    }

    response = rpc_client.call(json.dumps(body))
    return response
