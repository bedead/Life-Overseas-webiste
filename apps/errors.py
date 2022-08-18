from flask import Blueprint, render_template
from flask import current_app as app

errors = Blueprint(
    'errors', __name__,
    url_prefix='/errors'
)

# thrown when a unauthraized page is requested
# for unauthraized access
@errors.errorhandler(401)
def unauthraized_access(error):
    return render_template('errors/401.html'), 401


# error code used when access to the registered resource
# is forbidden (server understood the request but 
# can not fulfill it)
@errors.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403


# error thrown when there is no such page
# found as request by client
@errors.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


# error occured when there is problem with 
# the website's server
@errors.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500


# something wrong with a website's server
# communication, (can be due to loss of internet)
@errors.errorhandler(502)
def bad_gateway(error):
    return render_template('errors/502.html'), 502


# response code which indicates that the server 
# is not ready to handle the request
@errors.errorhandler(503)
def service_unavailable(error):
    return render_template('errors/503.html'), 503


# web server aren't communicating with each
# other fast enough
@errors.errorhandler(504)
def service_unavailable(error):
    return render_template('errors/504.html'), 504

    