from typing import List
from sqlalchemy import select
from fastapi import FastAPI, HTTPException

from activemq.listener import MyListener
from activemq.producers.lockbox_producer import LockBoxProducer
from dao.model import Post, PostResponse, PostCreate
from dao.database import Base, engine
from dao.dependencies import db_dependency

from activemq.active_mq import ActiveMQ
from utils.env_variables import ACTIVEMQ_USER, ACTIVEMQ_PASSWORD, ACTIVEMQ_PORT, ACTIVEMQ_HOST

app = FastAPI()

Base.metadata.create_all(bind=engine)
print("Database initialized successfully.")

# ActiveMQ connection manager
mq = ActiveMQ(
    host=ACTIVEMQ_HOST,
    port=ACTIVEMQ_PORT,
    username=ACTIVEMQ_USER,
    password=ACTIVEMQ_PASSWORD,
    queues=["/queue/lockbox"],
)
connection = mq.connect(listener=None)
listener = MyListener(connection=connection)

lockbox_producer = LockBoxProducer(connection)

@app.post("/produce/")
def publish_message(post: PostCreate):
    print("Publishing...")
    print(f'Request: {post}')
    json_post = post.model_dump_json()
    lockbox_producer.send_message(json_post)
    print(f"Response: {post}")
    return {"status","success"}


@app.get("/posts/", response_model=List[PostResponse])
def read_heroes(db: db_dependency) -> List[PostResponse]:
    try:
        heroes = db.execute(select(Post)).scalars().all()  # Fetch all rows
        return [PostResponse.model_validate(hero) for hero in heroes]
    except Exception as e:
        print(f"error retrieving users {e}")
        raise HTTPException(500, "Error retrieving users!")
