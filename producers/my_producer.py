from active_mq import ActiveMQ
from .producer import Producer
from dotenv import load_dotenv
import os

load_dotenv()

class LockBoxProducer(Producer):
    def __init__(self):
        super().__init__(os.getenv("QUEUE"))
        self.active_mq = ActiveMQ()

    def send_message(self, message: str):
        try:
            connection = self.active_mq.connect()
            connection.send(body=message, destination=self.queue)
            print(f"Message sent to {self.queue}: {message}")
            connection.disconnect()
        except Exception as e:
            print(f"Error sending message to {self.queue}: {e}")