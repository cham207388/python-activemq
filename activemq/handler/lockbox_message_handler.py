import json
from datetime import datetime
from tzlocal import get_localzone


class LockBoxMessageHandler:
    def __init__(self, elis_producer):
        self.elis_producer = elis_producer

    def handle_message(self, message):
        print(f"LockBoxMessageHandler received: {message}")
        try:
            # Parse and modify the message
            message_data = json.loads(message)
            local_timezone = get_localzone()
            message_data["timestamp"] = datetime.now(local_timezone).strftime("%d:%m:%Y %H:%M:%S")
            modified_message = json.dumps(message_data)

            # Forward the modified message to Elis queue
            self.elis_producer.send_message(modified_message)
            print(f"Forwarded modified message to Elis queue: {modified_message}")
        except json.JSONDecodeError as e:
            print(f"Error decoding message in LockBoxMessageHandler: {e}")