from sqlalchemy import create_engine
from utils.env_variables import db_engine_url

engine = create_engine(db_engine_url)

# Test connection
with engine.connect() as connection:
    result = connection.execute("SELECT 1")
    print(f"Database connection successful: {result.scalar()}")