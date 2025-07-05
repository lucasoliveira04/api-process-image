import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PIL import Image
from mensageria.rabbitmq_client import get_channel
from dotenv import load_dotenv
from model.image_model import ImageModel
from cache.redis_cache_configuration import redis_client

import json


load_dotenv()

def process_image_task(body):
    data = json.loads(body)
    image_path = data["imagePath"]
    image_id = data["imageId"]
    image_width = int(data["imageWidth"])
    image_height = int(data["imageHeight"])
    filename = data["imageName"]
    new_path = f"/mnt/imagens/{filename}"
    

    try:
        with Image.open(image_path) as img:
            img = img.resize((image_width, image_height))
            img.save(new_path)
    

        image_model = ImageModel(
            imageId=image_id,
            imageName=filename,
            imageWidth=image_width,
            imageHeight=image_height,
            imagePath=image_path,
            imagePathFinal=new_path,
            imageStatus="processed"
            
        )

        redis_client.set(image_id, json.dumps(image_model.to_dict()))
        print(f"Imagem processada: {filename}")
    except Exception as e:
        print(f"Erro ao processar imagem: {e}")

def main():
    connection, channel = get_channel()
    channel.queue_declare(queue="image_processing")

    def callback(ch, method, properties, body):
        process_image_task(body)

    print("[*] Worker aguardando mensagens...")
    channel.basic_consume(queue="image_processing", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print(f"Erro na conexão com RabbitMQ: {e}")
            print("Tentando reconectar em 5 segundos...")
            time.sleep(5)

