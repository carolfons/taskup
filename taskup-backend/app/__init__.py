from flask import Flask
from flask_cors import CORS
from app.routes.task_routes import task_bp
from app.config.settings import Config
from app.extensions import db


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    #initialize extensions
    db.init_app(app)
    CORS(app)
    
    # Register Blueprints (modular routes)
    app.register_blueprint(task_bp, url_prefix="/tasks")

    return app
    