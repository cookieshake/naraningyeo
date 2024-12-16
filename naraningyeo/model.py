from datetime import datetime

from pydantic import BaseModel


class Sender(BaseModel):
    id: str | None
    name: str

class Room(BaseModel):
    id: str | None
    name: str

class IncomingMessage(BaseModel):
    message: str
    sender: Sender
    room: Room

class OutgoingMessage(BaseModel):
    do_reply: bool
    message: str | None

class Chat(BaseModel):
    room_id: int
    sender_name: str
    message: str
    timestamp: datetime

class MultiChatLog(BaseModel):
    chats: list[Chat]
