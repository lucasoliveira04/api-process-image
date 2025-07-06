from pika import PlainCredentials, ConnectionParameters, BlockingConnection, exceptions
import os
import time

from dotenv import load_dotenv

load_dotenv()

def get_connection(max_retries=10, delay=3):
    creds = PlainCredentials(
        os.getenv("RABBITMQ_USER", "guest"),
        os.getenv("RABBITMQ_PASSWORD", "guest"),
    )
    params = ConnectionParameters(
        host=os.getenv("RABBITMQ_HOST", "rabbitmq"),
        port=int(os.getenv("RABBITMQ_PORT", 5672)),
        virtual_host=os.getenv("RABBITMQ_VIRTUAL_HOST", "/"),
        credentials=creds,
    )

    for attempt in range(1, max_retries + 1):
        try:
            return BlockingConnection(params)
        except exceptions.AMQPConnectionError as e:
            print(f"[{attempt}/{max_retries}] RabbitMQ not available, retrying in {delay}s...")
            time.sleep(delay)
    raise RuntimeError("Could not connect to RabbitMQ after several attempts")

def get_channel():
    connection = get_connection()
    channel = connection.channel()
    return connection, channel


__all__ = ["get_connection", "get_channel"]