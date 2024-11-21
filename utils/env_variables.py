from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

ACTIVEMQ_USER = os.getenv("ACTIVEMQ_USER")
ACTIVEMQ_PASSWORD = os.getenv("ACTIVEMQ_PASSWORD")
ACTIVEMQ_HOST = os.getenv("ACTIVEMQ_HOST")
ACTIVEMQ_PORT = os.getenv("ACTIVEMQ_PORT")
QUEUE = os.getenv("QUEUE")

db_engine_url = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
