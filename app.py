from flask import Flask
from controllers.animal_controller import animal_blueprint

app = Flask(__name__)

app.register_blueprint(animal_blueprint)