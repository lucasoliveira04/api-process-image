from mensageria.rabbitmq_client import get_channel
from PIL import Image
from models.image_model import ImageModel
from cache.redis_cache_configuration import redis_client

def process_image(image: ImageModel):
    try:
        img = Image.open(image.original_path)

        resized = img.resize((128, 128))
        resized.save(image.processed_path)

        image.status = "processed"
        redis_client.set(image.id, image.json())
        print(f"Image {image.id} processed successfully.")

    except Exception as e:
        image.status = "error"
        redis_client.set(image.id, image.json())
        print(f"Error processing image {image.id}: {e}")

def callback(ch, method, properties, body):
    image_id = body.decode()
    print("Message received:", image_id)

    data = redis_client.get(image_id)

    if not data:
        print(f"Image {image_id} not found in cache.")
        return
    
    image = ImageModel.parse_raw(data)
    image.status = "processing"
    redis_client.set(image.id, image.json())

    process_image(image)

channel, connection = get_channel()

channel.basic_consume(queue="image_processing", on_message_callback=callback, auto_ack=True)

print("Starting image processing worker...")
channel.start_consuming()