from model.image_model import ImageModel
from mensageria.rabbitmq_client import get_channel
from uuid import uuid4
from pathlib import Path
import json


def get_image_folder():
    folder = Path("/mnt/imagens")
    folder.mkdir(parents=True, exist_ok=True)
    return folder

def image_services(file, image_width: int, image_height: int):
    try:
        image_id = str(uuid4())
        filename = f"{image_id}_{file.filename}"
        folder = get_image_folder()
        file_path = folder / filename
        file.save(file_path)

        message = {
            "imageId": image_id,
            "imageName": filename,
            "imageWidth": int(image_width),
            "imageHeight": int(image_height),
            "imagePath": str(file_path)
        }

        print("Message sent to queue:")
        print(json.dumps(message, indent=2))

        connection, channel = get_channel()
        channel.queue_declare(queue='image_processing')
        channel.basic_publish(
            exchange='',
            routing_key='image_processing',
            body=json.dumps(message)
        )
        connection.close()

        return {"message": "Image processing started successfully", "imageId": image_id}
    except Exception as e:
        print(f"Error processing image: {e}")
        return {"error": str(e)}
