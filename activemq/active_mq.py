import stomp
import json
from sqlalchemy.orm import Session

from dao.model import Post, convert_to_post
from utils.env_variables import ACTIVEMQ_USER, ACTIVEMQ_PASSWORD, ACTIVEMQ_PORT, ACTIVEMQ_HOST
from dao.database import SessionLocal


class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print(f'Error: {frame.body}')
    def on_message(self, frame):
        print(f'Received message: {frame.body}')
        print(f'type: {type(frame.body)}')
        post = sanitize_post(frame.body)
        save_post_to_db(post, SessionLocal())
        print(f'Saved post to db...')

class ActiveMQ:
    def __init__(self):
        self.host = ACTIVEMQ_HOST
        self.port = ACTIVEMQ_PORT
        self.username = ACTIVEMQ_USER
        self.password = ACTIVEMQ_PASSWORD
        self.connection = stomp.Connection([(ACTIVEMQ_HOST, ACTIVEMQ_PORT)])

    def connect(self):
        print(f'host: {self.host}, port: {self.port}, username: {self.username}, password: {self.password}')
        self.connection.set_listener('', MyListener())
        self.connection.connect(self.username, self.password, wait=True)
        return self.connection

def save_post_to_db(post: Post, db: Session):
    try:
        save_post = convert_to_post(post)
        print("Saving...")
        db.add(save_post)
        db.commit()
    except Exception as e:
        print(f"Failed to save hero to database: {e}")

def sanitize_post(body):

    post_data = json.loads(body)  # Parse the JSON string to a dictionary
    post = Post(**post_data) # Cast dictionary to Post
    return post