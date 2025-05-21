import os
from flask import Flask
from flask_cors import CORS
import logging
from config import config
from models import db
from routes import api

def create_app(config_name='default'):
    """
    Create and configure the Flask application
    
    Args:
        config_name (str): Configuration to use (development, production, default)
        
    Returns:
        Flask: Configured Flask application
    """
    # Create Flask app
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Enable CORS
    CORS(app)
    
    # Set up logging
    if not app.debug:
        logging.basicConfig(level=logging.INFO)
    
    # Initialize database
    db.init_app(app)
    
    # Create instance directory
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Register blueprint
    app.register_blueprint(api, url_prefix='/api')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Root route
    @app.route('/')
    def index():
        return {
            'name': 'Data Visualization Pricing Analyst Form API',
            'version': '1.0.0',
            'documentation': '/api'
        }
    
    # API documentation route
    @app.route('/api')
    def api_docs():
        return {
            'endpoints': [
                {
                    'path': '/api/submissions',
                    'methods': ['GET', 'POST'],
                    'description': 'List or create submissions'
                },
                {
                    'path': '/api/submissions/<id>',
                    'methods': ['GET', 'PUT', 'DELETE'],
                    'description': 'Get, update, or delete a specific submission'
                },
                {
                    'path': '/api/submissions/<id>/pdf',
                    'methods': ['GET'],
                    'description': 'Generate and download PDF for a submission'
                },
                {
                    'path': '/api/submissions/stats',
                    'methods': ['GET'],
                    'description': 'Get statistics about submissions'
                }
            ]
        }
    
    return app

if __name__ == '__main__':
    # Get configuration from environment variable or use development
    config_name = os.getenv('FLASK_CONFIG', 'development')
    app = create_app(config_name)
    
    # Run the app
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)