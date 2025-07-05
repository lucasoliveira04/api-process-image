from redis import StrictRedis
from dotenv import load_dotenv
import os

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_username = os.getenv("REDIS_USERNAME")
redis_password = os.getenv("REDIS_PASSWORD")

redis_client = StrictRedis( 
    host=redis_host, # type: ignore
    port=redis_port, # type: ignore
    username=redis_username,
    password=redis_password,
    decode_responses=True
)

try:
    redis_client.ping()
    print("Redis connection successful")
except Exception as e:
    print(f"Redis connection failed: {e}")

__all__ = ["redis_client"]