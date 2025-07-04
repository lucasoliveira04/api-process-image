import uuid
import json
from pika import BlockingConnection, ConnectionParameters
from models.image_model import ImageModel
from cache.redis_cache_configuration import redis_client
from mensageria.rabbitmq_client import publish_message

def handle_image_upload(file):
    image_id = str(uuid.uuid4())
    filename = file.filename
    original_path = f"/uploads/{filename}"
    processed_path = f"/processed/{filename}"
    file.save(original_path)

    image = ImageModel(
        id=image_id,
        filename=filename,
        status="pending",
        original_path=original_path,
        processed_path=processed_path
    )


    redis_client.set(image_id, image.json())

    # enviar para fila do RabbitMQ
    publish_message(image_id)
    

    return {"image_id": image_id, "status": "pending"}