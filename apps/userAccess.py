from flask import Blueprint, render_template
from flask import current_app as app

users = Blueprint(
    'users', __name__,
    url_prefix='/access'
)

@users.route('/')
def access():
    return render_template('accessed.html')