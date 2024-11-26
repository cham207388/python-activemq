from .producer import Producer

class ElisProducer(Producer):
    def __init__(self, connection):
        super().__init__("/queue/elis")
        self.connection = connection

    def send_message(self, message: str):
        try:
            connection = self.connection
            connection.send(body=message, destination=self.queue)
            print(f"Message sent to {self.queue}: {message}")
            connection.disconnect()
        except Exception as e:
            print(f"Error sending message to {self.queue}: {e}")