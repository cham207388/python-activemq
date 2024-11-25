from stomp import ConnectionListener


class MyListener(ConnectionListener):
    def __init__(self, connection, consumers):
        self.connection = connection
        self.consumers = consumers

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