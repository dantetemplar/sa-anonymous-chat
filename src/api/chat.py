from datetime import datetime, timezone

from pydantic import BaseModel
import sqlite3


class Message(BaseModel):
    text: str
    timestamp: datetime


# noinspection SqlNoDataSourceInspection
class Chat:
    def __init__(self, db_path='chat.sqlite3'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_message(self, text: str):
        timestamp = datetime.now(timezone.utc).isoformat()
        self.conn.execute(
            'INSERT INTO messages (text, timestamp) VALUES (?, ?)',
            (text, timestamp)
        )
        self.conn.commit()

    def get_message_count(self) -> int:
        cursor = self.conn.execute('SELECT COUNT(*) FROM messages')
        count = cursor.fetchone()[0]
        return count

    def get_all_messages(self) -> list[Message]:
        cursor = self.conn.execute('SELECT text, timestamp FROM messages ORDER BY id')
        rows = cursor.fetchall()
        messages = [
            Message(
                text=text,
                timestamp=datetime.fromisoformat(timestamp)
            )
            for text, timestamp in rows
        ]
        return messages

    def delete_all_messages(self):
        self.conn.execute('DELETE FROM messages')
        self.conn.commit()


chat_instance = Chat()
