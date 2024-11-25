import stomp
import json
from sqlalchemy.orm import Session

from dao.model import Post, convert_to_post
from utils.env_variables import ACTIVEMQ_USER, ACTIVEMQ_PASSWORD, ACTIVEMQ_PORT, ACTIVEMQ_HOST


class ActiveMQ:
    def __init__(self):
        self.host = ACTIVEMQ_HOST
        self.port = ACTIVEMQ_PORT
        self.username = ACTIVEMQ_USER
        self.password = ACTIVEMQ_PASSWORD
        self.connection = None

    def connect(self):
        print(f"Connecting host: {self.host}, port: {self.port}, username: {self.username} {self.password}")
        if not self.connection or not self.connection.is_connected():
            self.connection = stomp.Connection([(self.host, self.port)])
            self.connection.connect(self.username, self.password, wait=True)
        return self.connection

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.disconnect()
            self.connection = None

# def save_post_to_db(post: Post, db: Session):
#     try:
#         save_post = convert_to_post(post)
#         print("Saving...")
#         db.add(save_post)
#         db.commit()
#     except Exception as e:
#         print(f"Failed to save hero to database: {e}")
#
# def sanitize_post(body):
#
#     post_data = json.loads(body)  # Parse the JSON string to a dictionary
#     post = Post(**post_data) # Cast dictionary to Post
#     return post