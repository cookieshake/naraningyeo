from typing import Union

from fastapi import FastAPI, Request
from loguru import logger

from naraningyeo.model import IncomingMessage, OutgoingMessage

app = FastAPI()

@app.get("/")
async def get_root():
    return {"Hello": "World"}

@app.post("/")
async def post_root(request: Request) -> OutgoingMessage:
    logger.debug(f"request: {await request.json()}")
    request = IncomingMessage.model_validate(await request.json())

    if "hello" in request.message:
        do_reply = True
    else:
        do_reply = False
    return OutgoingMessage(do_reply=do_reply, message="Hello, World!")
