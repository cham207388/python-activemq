from stomp import ConnectionListener


class MyListener(ConnectionListener):
    def __init__(self, connection, dispatcher):
        self.connection = connection
        self.dispatcher = dispatcher

    def on_error(self, frame):
        print(f"Error: {frame.body}")

    def on_message(self, frame):
        destination = frame.headers.get("destination", "")
        print(f"Received message from {destination}: {frame.body}")
        self.dispatcher.dispatch_message(destination, frame.body)