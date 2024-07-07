# Import the threading module for creating background threads
import threading
# Import necessary Flask modules
from flask import Blueprint, render_template, url_for, request
# Import modules from the trend package
from trend import indis, oscs, patts
# Import the indices module from the strategies package
from strategies import indices
# Import the send_mail function
from send_mail import send_mail

# Create a Blueprint for the main application
main = Blueprint('main', __name__)

# Define the route for the home page
@main.route('/')
def index():
    # Render the index_min.html template with the indis, oscs, and patts data
    return render_template('index_min.html', indis=indis, oscs=oscs, patts=patts)

# Define the route for the about page
@main.route('/about')
def about():
    # Render the about_min.html template
    return render_template('about_min.html')

# Define the route for the strategies page
@main.route('/strategies')
def strategies():
    # Render the strategies_min.html template with the indices and indis data
    return render_template('strategies_min.html', indices=indices, indis=indis)

# Define the route for the contact page
@main.route('/contact')
def contact():
    # Render the contact_min.html template
    return render_template('contact_min.html')

# Define the route for the success page
@main.route('/success',methods=['GET', 'POST'] )
def success():
    # Handle POST requests to send an email
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        
        # Move the send_mail function to a background thread
        t1 = threading.Thread(target=send_mail, args=[email])
        t1.start()

        # Render the success_min.html template with the name and email data
        return render_template('success_min.html', name=name, email=email)

# Define a custom error handler for 404 errors (Page Not Found)  
@main.app_errorhandler(404)
def not_found(e):
    # Render the 404_min.html template with a 404 status code
    return render_template('404_min.html'), 404

# Define a custom error handler for 500 errors (Internal Server Error)
@main.app_errorhandler(500)
def internal_server_error(e):
    # Render the 500_min.html template with a 500 status code
    return render_template('500_min.html'), 500



