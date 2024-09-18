from datetime import datetime, timezone

from pydantic import BaseModel


class Message(BaseModel):
    text: str
    timestamp: datetime


class Chat:
    def __init__(self):
        self.messages: list[Message] = []

    def add_message(self, text: str):
        message = Message(text=text, timestamp=datetime.now(timezone.utc))
        self.messages.append(message)

    def get_message_count(self) -> int:
        return len(self.messages)

    def get_all_messages(self) -> list[Message]:
        return self.messages


chat_instance = Chat()
