import json
from dao.database import SessionLocal
from dao.model import convert_to_post
from .consumer import Consumer


class ElisConsumer(Consumer):
    def __init__(self):
        super().__init__("/queue/elis")

    def process_message(self, message: str):
        print(f"Elis consumer received: {message}")
        try:
            # Convert dictionary to Post ORM object
            post = convert_to_post(message_data)

            session = SessionLocal()
            session.add(post)
            session.commit()
            session.close()
            print("Message saved to database.")
        except Exception as e:
            print(f"Error saving message to database: {e}")