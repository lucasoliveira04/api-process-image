from flask import Flask
from controllers.image_controller import image_controller

app = Flask(__name__)
app.register_blueprint(image_controller)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)