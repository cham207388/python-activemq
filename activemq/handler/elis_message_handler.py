class ElisMessageHandler:
    def handle_message(self, message):
        """
        Process messages received from the Elis queue.
        :param message: The message body
        """
        print(f"ElisMessageHandler received: {message}")
        # Add custom logic for processing Elis messages