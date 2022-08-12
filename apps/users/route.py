from flask import Blueprint
from flask import current_app as app

users = Blueprint(
    'users_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/access'
)
