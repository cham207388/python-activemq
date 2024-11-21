from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from pydantic import BaseModel, Field
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
    title: str = Field(min_length=3, max_length=15)
    content: str = Field(min_length=3, max_length=15)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'Peace',
                'content': 'Cooler than Dad',
            }
        }

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    # published: bool
    # created_at: datetime

    # Enable compatibility with ORM models (e.g., SQLModel)
    model_config = {
        "from_attributes": True  # This allows attribute access from ORM objects
    }

def convert_to_post(request: PostCreate) -> Post:
    return Post(
        id=None,
        content=request.content,
        title=request.title,
    )