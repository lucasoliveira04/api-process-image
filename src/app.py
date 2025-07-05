from controller.image_controller import image_controller
from flask import Flask

app = Flask(__name__)
app.register_blueprint(image_controller, url_prefix='/api/images')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)