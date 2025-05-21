import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration class."""
    # Set the secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///instance/database.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Ensure instance folder exists
    @staticmethod
    def init_app(app):
        os.makedirs(os.path.join(app.instance_path), exist_ok=True)

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}