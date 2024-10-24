from flask import Flask
from dotenv import load_dotenv
from config import Config

load_dotenv()

def create_app():
    app = Flask(__name__)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.config.from_object(Config)

    return app
