from pika import BlockingConnection, ConnectionParameters, BasicProperties
import os
from dotenv import load_dotenv

load_dotenv()

rabbitmq_host = os.getenv("RABBITMQ_HOST")
rabbitmq_queue = os.getenv("RABBITMQ_QUEUE")

def get_channel():
    connection = BlockingConnection(ConnectionParameters(rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=rabbitmq_queue)
    return connection, channel

def publish_message(message: str):
    connection, channel = get_channel()
    channel.basic_publish(
        exchange="",
        routing_key=rabbitmq_queue,
        body=message
    )
    connection.close()