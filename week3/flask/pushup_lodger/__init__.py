from flask import Flask,Blueprint,render_template,url_for
def create_app():
    app=Flask(__name__)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import main as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app