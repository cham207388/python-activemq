class MessageDispatcher:
    def __init__(self):
        """
        Initialize the message dispatcher with an empty set of handlers.
        """
        self.handlers = {}

    def register_handler(self, destination, handler):
        """
        Register a handler for a specific destination.
        :param destination: The destination queue
        :param handler: The handler instance
        """
        self.handlers[destination] = handler

    def dispatch_message(self, destination, message):
        """
        Dispatch a message to the appropriate handler.
        :param destination: The destination queue
        :param message: The message body
        """
        handler = self.handlers.get(destination)
        if handler:
            handler.handle_message(message)
        else:
            print(f"No handler registered for destination: {destination}")