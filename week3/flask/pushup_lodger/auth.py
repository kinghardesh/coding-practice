from flask import Blueprint, render_template

# Initialize the auth blueprint
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    # Initially returns text, later updated to render login.html
    return render_template('login.html')

@auth.route('/signup')
def signup():
    # Initially returns text, later updated to render signup.html
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    # Logout usually redirects or handles logic, but for now:
    return "This is the logout page"