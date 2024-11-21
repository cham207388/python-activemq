from typing import List
from sqlalchemy import select
from fastapi import FastAPI, HTTPException
from dao.model import Post, PostResponse, PostCreate
from producer import send_message
from dao.database import Base, engine
from dao.dependencies import db_dependency

app = FastAPI()


Base.metadata.create_all(bind=engine)
print("Database initialized successfully.")

@app.post("/produce/", response_model=PostResponse)
def publish_message(post: PostCreate) -> PostResponse:
    print("Publishing...")
    print(f'Request: {post}')
    json_post = post.model_dump_json()
    send_message(json_post)
    print(f"Response: {post}")
    return PostResponse.model_validate(post)


@app.get("/posts/", response_model=List[PostResponse])
def read_heroes(db: db_dependency) -> List[PostResponse]:
    try:
        heroes = db.execute(select(Post)).scalars().all()  # Fetch all rows
        return [PostResponse.model_validate(hero) for hero in heroes]
    except Exception as e:
        print(f"error retrieving users {e}")
        raise HTTPException(500, "Error retrieving users!")
