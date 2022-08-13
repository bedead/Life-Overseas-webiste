from flask import Blueprint, render_template
from flask import current_app as app

errors = Blueprint(
    'errors', __name__,
    url_prefix='/errors'
)


@errors.route('/401')
def error_401():
    pass
@errors.route('/404')
def error_404():
    pass
@errors.route('/500')
def error_500():
    pass
@errors.route('/304')
def error_304():
    return 'Page Not Found'