from .producer import Producer


class LockBoxProducer(Producer):
    def __init__(self, connection):
        super().__init__("/queue/lockbox")
        self.connection = connection

    def send_message(self, message: str):
        try:
            print(f"Sending message to {self.queue}: {message}")
            self.connection.send(destination=self.queue, body=message)
            print(f"Message sent to {self.queue}.")
            self.connection.disconnect()
        except Exception as e:
            print(f"Error sending message to {self.queue}: {e}")