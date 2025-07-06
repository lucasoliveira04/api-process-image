from flask import Blueprint, request, jsonify
from services.image_services import image_services
from cache.redis_cache_configuration import redis_client
import json

image_controller = Blueprint('image_controller', __name__)

@image_controller.route('/process/<image_width>/<image_height>', methods=['POST'])
def process_image(image_width, image_height):
    if "file" not in request.files:
        return {"error": "No file part in the request"}, 400

    if not image_width or not image_height:
        return {"error": "Width and Height are required"}, 400
    
    file = request.files['file']
    result = image_services(file, image_width, image_height)

    if result.get("error"):
        return result, 400 
    
    return result, 200

@image_controller.route('/<image_id>', methods=['GET'])
def get_image_by_id(image_id):
    image_data = redis_client.get(image_id)
    if not image_data:
        return {"error": "Image not found"}, 404

    image_data = json.loads(str(image_data))
    print(f"Dados da imagem para ID {image_id}: {json.dumps(image_data, indent=2)}")
    return jsonify(image_data), 200
