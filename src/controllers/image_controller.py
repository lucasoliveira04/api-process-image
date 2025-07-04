from flask import Blueprint, request, jsonify
from services.image_services import handle_image_upload

image_controller = Blueprint('image_controller', __name__)

@image_controller.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    result = handle_image_upload(file)
    return jsonify(result), 200