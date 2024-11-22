from .producer import Producer

class ElisProducer(Producer):
    def __init__(self, connection):
        super().__init__("/queue/elis")
        self.connection = connection

    def send_message(self, message):
        if not self.connection.is_connected():
            raise ConnectionError("Connection to ActiveMQ is not active.")

        print(f"Sending message to {self.queue}: {message}")
        self.connection.send(destination=self.queue, body=message)
        print(f"Message sent to {self.queue}.")