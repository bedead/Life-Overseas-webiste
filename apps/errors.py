from flask import Blueprint, render_template
from flask import current_app as app

errors = Blueprint(
    'errors', __name__,
    url_prefix='/errors'
)


@errors.route('/401')
def error_401():
    return render_template('errors/401.html')

@errors.route('/404')
def error_404():
    return render_template('errors/404.html')
    
@errors.route('/500')
def error_500():
    return render_template('errors/500.html')
    
@errors.route('/304')
def error_304():
    return render_template('errors/304.html')