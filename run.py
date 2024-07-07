# Import necessary Flask modules
from flask import Flask, Blueprint
# Import Jinja2 for template rendering
import jinja2
# Import the main blueprint from the routes module
from routes import main

# Create an application object using the factory pattern
def create_app(config_file='settings.py'):
    # Initialize a Flask application
    app = Flask(__name__)

    # Load configuration settings from the specified file
    app.config.from_pyfile(config_file)

    # Register the main blueprint with the application
    app.register_blueprint(main)
    
    # Ensure access to Python built-in functions within application templates
    app.jinja_env.globals.update(zip=zip)

    # Return the configured Flask application
    return app
