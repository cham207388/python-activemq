import ssl
from stomp import ConnectionListener, Connection12
import time

# Broker details
broker_host = "b-c3c50510-2b1d-4db1-bda0-f7ed7c9863af-1.mq.us-east-2.amazonaws.com"
broker_port = 61614  # Default port for STOMP over SSL
username = 'ExampleUser'
password = 'changemelonger'

# SSL context setup
# SSL context setup (disable verification for testing)
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False  # Disable hostname verification
ssl_ctx.verify_mode = ssl.CERT_NONE  # Disable certificate verification

# Listener class
class MyListener(ConnectionListener):
    def on_error(self,  message):
        print(f'Received an error: {message}')
    def on_message(self,  message):
        print(f'Received a message: {message}')

# Establish connection
conn = Connection12(
    host_and_ports=[(broker_host, broker_port)],
    heartbeats=(4000, 4000)  # Optional: configure heartbeats
)

# Assign SSL context
conn.set_ssl([(broker_host, broker_port)], ssl_ctx)

# Add listener and connect
conn.set_listener('', MyListener())
conn.connect(username, password, wait=True)

# Destination queue
destination = '/queue/test'

# Send a message
conn.send(body='Hello, Amazon MQ!', destination=destination)

# Subscribe to the queue
conn.subscribe(destination=destination, id=1, ack='auto')

# Keep the connection alive to receive messages
time.sleep(5)  # Adjust sleep time as needed

# Disconnect
conn.disconnect()