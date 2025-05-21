from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Initialize SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """Initialize the database with the Flask app"""
    # Configure SQLite database URI
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'pricing.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the db with the Flask app
    db.init_app(app)
    
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()