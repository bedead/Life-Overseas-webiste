# @author Satyam Mishra

from flask import Flask
from apps.packages.pyrebase import *


def create_app():
    """Create Flask application."""
    name = "Life Overseas"
    app = Flask(name, instance_relative_config=False)
    # selecting config file for application to run
    # Basic config, Dev, and Prod
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Import parts of our application
        from . import admin
        from . import main
        from . import userAccess
        from . import userLogin
        from . import errors
        
        # Register Blueprints
        app.register_blueprint(admin.admin)
        app.register_blueprint(main.main)
        app.register_blueprint(userLogin.userLogin)
        app.register_blueprint(userAccess.users)
        app.register_blueprint(errors.errors)
        # returning app
        return app