
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from utils.env_variables import db_engine_url

engine = create_engine(db_engine_url, echo=True)

print(f'Connected to database...')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
