import json
from dao.database import SessionLocal
from ..producers.elis_producer import ElisProducer
from .consumer import Consumer


class LockBoxConsumer(Consumer):
    def __init__(self):
        super().__init__("/queue/lockbox")
        self.elis_producer = ElisProducer()

    def process_message(self, message: str):
        print(f"Lockbox consumer received: {message}")
        try:
            # Modify the message
            message_data = json.loads(message)
            message_data["id"] = "lockboxid"
            modified_message = json.dumps(message_data)

            # Forward the modified message to /queue/elis
            self.elis_producer.send_message(modified_message)
        except json.JSONDecodeError as e:
            print(f"Error decoding message in lockbox consumer: {e}")