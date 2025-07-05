from flask import Blueprint, request, jsonify
from services.image_services import image_services

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

@image_controller.route('/', methods=['GET'])
def get_images():
    return {"images": [], "message": "No images found."}, 404
