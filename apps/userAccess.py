from flask import Blueprint, render_template
from flask import current_app as app

users = Blueprint(
    'users', __name__,
    url_prefix='/access'
)

@users.route('/')
def access():
    # if not auth return to page 401 error
    # else access page
    return render_template('loged_users/accessed.html')