# Import the environ module from the os package to access environment variables
from os import environ

# Retrieve the SECRET_KEY from environment variables for secure configurations
SECRET_KEY = environ.get('SECRET_KEY')
