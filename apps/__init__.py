from flask import Flask, flash, redirect, render_template, request, url_for
from apps.pyrebase import *


def create_app():
    """Create Flask application."""
    name = "Life Overseas"
    app = Flask(name, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Import parts of our application
        from .admin import route
        from .main import route
        from .userLogin import route
        from .users import route

        # Register Blueprints
        app.register_blueprint(admin.route.admin)
        app.register_blueprint(main.route.main)
        app.register_blueprint(userLogin.route.userLogin)
        app.register_blueprint(users.route.users)


        return app