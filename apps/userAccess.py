from flask import Blueprint
from flask import current_app as app

users = Blueprint(
    'users', __name__,
    url_prefix='/access'
)
