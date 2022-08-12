from flask import Flask, flash, redirect, render_template, request, url_for
from apps.packages.pyrebase import *


def create_app():
    """Create Flask application."""
    name = "Life Overseas"
    app = Flask(name, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Import parts of our application
        from . import admin
        from . import main
        from . import userAccess
        from . import userLogin
        
        # Register Blueprints
        app.register_blueprint(admin.admin)
        app.register_blueprint(main.main)
        app.register_blueprint(userLogin.userLogin)
        app.register_blueprint(userAccess.users)


        return app