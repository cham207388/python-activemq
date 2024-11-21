from stomp import ConnectionListener
from .consumers.elis_consumer import ElisConsumer
from .consumers.lockbox_consumer import LockBoxConsumer


class MyListener(ConnectionListener):
    def __init__(self, connection):
        self.connection = connection
        self.consumers = {
            "/queue/lockbox": LockBoxConsumer(),
            "/queue/elis": ElisConsumer(),
        }

    def on_error(self, frame):
        print(f"Error: {frame.body}")

    def on_message(self, frame):
        destination = frame.headers.get("destination", "")
        print(f"Received message from {destination}: {frame.body}")

        consumer = self.consumers.get(destination)
        if consumer:
            consumer.process_message(frame.body)
        else:
            print(f"No consumer available for destination: {destination}")