import stomp

from utils.env_variables import ACTIVEMQ_USER, ACTIVEMQ_PASSWORD, ACTIVEMQ_PORT, ACTIVEMQ_HOST


class ActiveMQ:
    def __init__(self):
        self.host = ACTIVEMQ_HOST
        self.port = ACTIVEMQ_PORT
        self.username = ACTIVEMQ_USER
        self.password = ACTIVEMQ_PASSWORD
        self.connection = None

    def connect(self):
        if not self.connection or not self.connection.is_connected():
            self.connection = stomp.Connection([(self.host, self.port)])
            self.connection.connect(self.username, self.password, wait=True)
        return self.connection

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.disconnect()
            self.connection = None