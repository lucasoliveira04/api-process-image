from redis import StrictRedis
from dotenv import load_dotenv
import os

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_username = os.getenv("REDIS_USERNAME")
redis_password = os.getenv("REDIS_PASSWORD")

redis_client = StrictRedis(
    host=redis_host,
    port=redis_port,
    username=redis_username,
    password=redis_password,
    decode_responses=True
)

__all__ = ["redis_client"]