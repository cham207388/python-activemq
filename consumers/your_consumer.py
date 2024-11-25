import json
from datetime import datetime
from tzlocal import get_localzone

from active_mq import ActiveMQ
from .consumer import Consumer


class YourConsumer(Consumer):

    def __init__(self):
        super().__init__("/queue/Consumer.B.VirtualTopic.mytopic")
        self.mq = ActiveMQ()

    def process_message(self, message: str):
        print(f"Lockbox consumer received: {message}")
        try:
            # Modify the message
            message_data = json.loads(message)
            # message_data["timestamp"] = datetime.now(timezone.utc).strftime("%d:%m:%Y %H:%M:%S")
            local_timezone = get_localzone()
            message_data["timestamp"] = datetime.now(local_timezone).strftime("%d:%m:%Y %H:%M:%S")
            modified_message = json.dumps(message_data)
            print(f"modified message: {modified_message}")

        except json.JSONDecodeError as e:
            print(f"Error decoding message in lockbox consumer: {e}")

    def subscribe(self, index: int):
        self.mq.connect().subscribe(destination=self.queue, id=index, ack='auto')