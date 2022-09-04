# @author Satyam Mishra

from flask import Blueprint, abort, render_template, session

users = Blueprint(
    'users', __name__,
    url_prefix='/access'
)

@users.route('/')
def access():
    # if not auth return to page 401 error
    # else access page
    if session['email'] != None and session['localId'] != None:
        return render_template('loged_users/accessed.html')
    else:
        abort(401)