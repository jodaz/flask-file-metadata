from flask import Flask
from dotenv import load_dotenv
from config import Config
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)

    CORS(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.config.from_object(Config)

    return app
