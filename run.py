from flask import Flask, Blueprint
import jinja2
from routes import main

# Creating an application object using factory pattern
def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)

    app.register_blueprint(main)
    
    # Ensuring access to python built in function within application templates
    app.jinja_env.globals.update(zip=zip)

    return app
