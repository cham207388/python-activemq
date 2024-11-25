import json

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from pydantic import BaseModel, Field, ConfigDict
from dao.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    # published = Column(Boolean, server_default='TRUE')
    # created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __str__(self):
        return f"Post(id={self.id}, title={self.title}, content={self.content})"

    def __repr__(self):
        return self.__str__()

class PostCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    content: str = Field(min_length=3, max_length=50)

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'title': 'Peace',
                'content': 'Cooler than Dad',
            }
        }
    )

class PostResponse(BaseModel):
    id: int
    title: str
    content: str

    # Enable compatibility with ORM models (e.g., SQLModel)
    model_config = {
        "from_attributes": True  # This allows attribute access from ORM objects
    }

def to_post(data: dict) -> Post:

    return Post(title=data['title'], content=data['content'], id=None)

def convert_to_post(data: str) -> Post:
    print(f"=== {type(data)}")

    # Parse the JSON string into a dictionary
    message_data = json.loads(data)
    print(f"=== Message parsed, type: {type(message_data)}, content: {message_data}")

    return Post(title=data['title'], content=data['content'], id=None)