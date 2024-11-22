import stomp
import ssl
import logging


class ActiveMQ:
    def __init__(self, host, port, username, password, queues):
        """
        Initialize ActiveMQ connection details.
        :param host: ActiveMQ host
        :param port: ActiveMQ port
        :param username: ActiveMQ username
        :param password: ActiveMQ password
        :param queues: List of queues to subscribe to
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.queues = queues  # List of queues to subscribe to
        self.connection = None

        # Configure SSL
        self.ssl_ctx = ssl.create_default_context()
        self.ssl_ctx.check_hostname = False  # Disable hostname verification
        self.ssl_ctx.verify_mode = ssl.CERT_NONE  # Disable certificate verification

        # logging.basicConfig(level=logging.DEBUG)

    def connect(self, listener):
        """
        Establish connection to ActiveMQ and subscribe to queues.
        :param listener: Listener class instance
        :return: Active connection
        """
        print(f"Connecting to {self.host}:{self.port} as {self.username}...")

        if not self.connection or not self.connection.is_connected():
            try:
                self.connection = stomp.Connection12(
                    [(self.host, self.port)],
                    heartbeats=(4000, 4000)  # Optional: Configure heartbeats
                )
                self.connection.set_ssl([(self.host, self.port)], self.ssl_ctx)

                if listener:
                    self.connection.set_listener('', listener)

                self.connection.connect(self.username, self.password, wait=True)
                print("Connected successfully!")
            except Exception as e:
                print(f"Error connecting to ActiveMQ: {e}")
                raise

        return self.connection

    def disconnect(self):
        """
        Disconnect from ActiveMQ.
        """
        if self.connection and self.connection.is_connected():
            self.connection.disconnect()
            print("Disconnected from ActiveMQ.")
            self.connection = None