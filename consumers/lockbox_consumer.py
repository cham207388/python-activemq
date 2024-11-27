import json
from datetime import datetime
from tzlocal import get_localzone

from .consumer import Consumer


class LockboxConsumer(Consumer):
    def __init__(self, producer):
        super().__init__("/queue/lockbox")
        self.elis_producer = producer

    def process_message(self, message: str):
        print(f"Lockbox consumer received: {message}")
        try:
            # Modify the message
            message_data = json.loads(message)
            local_timezone = get_localzone()
            message_data["timestamp"] = datetime.now(local_timezone).strftime("%d:%m:%Y %H:%M:%S")
            modified_message = json.dumps(message_data)

            # Forward the modified message to /queue/elis
            self.elis_producer.send_message(modified_message)
        except json.JSONDecodeError as e:
            print(f"Error decoding message in lockbox consumer: {e}")
