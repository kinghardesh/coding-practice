from flask import Blueprint, render_template

# Initialize the main blueprint
# 'main' is the name of the blueprint used for url_for links
main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Renders the home page (index.html)
    return render_template('index.html')

@main.route('/profile')
def profile():
    # Renders the user profile page
    return render_template('profile.html')