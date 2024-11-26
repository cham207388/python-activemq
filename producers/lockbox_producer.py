from activemq.setup import ActiveMQ
from .producer import Producer


class LockboxProducer(Producer):
    def __init__(self, connection):
        super().__init__("/queue/lockbox")
        self.connection = connection

    def send_message(self, message: str):
        try:
            print("Publishing to lockbox queue...")
            self.connection.send(body=message, destination=self.queue)
            print(f"Message sent to {self.queue}: {message}")
            self.connection.disconnect()
        except Exception as e:
            print(f"Error sending message to {self.queue}: {e}")