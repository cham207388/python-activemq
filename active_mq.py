import stomp

from utils.env_variables import ACTIVEMQ_USER, ACTIVEMQ_PASSWORD, ACTIVEMQ_PORT, ACTIVEMQ_HOST


class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print(f'Error: {frame.body}')
    def on_message(self, frame):
        print(f'Received message: {frame.body}')

class ActiveMQ:
    def __init__(self):
        self.host = ACTIVEMQ_HOST
        self.port = ACTIVEMQ_PORT
        self.username = ACTIVEMQ_USER
        self.password = ACTIVEMQ_PASSWORD
        self.connection = stomp.Connection([(ACTIVEMQ_HOST, ACTIVEMQ_PORT)])

    def connect(self):
        print(f' ====== host: {self.host}')
        print(f' ====== port: {self.port}')
        print(f' ====== username: {self.username}')
        self.connection.set_listener('', MyListener())
        self.connection.connect(self.username, self.password, wait=True)
        return self.connection
