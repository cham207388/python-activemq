from stomp import ConnectionListener


class MyListener(ConnectionListener):
    def __init__(self, connection, lockbox_consumer, elis_consumer):
        self.connection = connection
        self.consumers = {
            "/queue/lockbox": lockbox_consumer,
            "/queue/elis": elis_consumer,
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