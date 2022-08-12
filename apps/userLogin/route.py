from flask import render_template, request
from flask import Blueprint
from flask import current_app as app
from apps.pyrebase import *


userLogin = Blueprint(
    'userLogin_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/user'
)

@userLogin.route("/signin",methods=["GET","POST"])
def user_signin():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    
    return render_template("sign_in")

@userLogin.route("/signup",methods=["GET","POST"])
def user_signup():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    if request.method=="POST":
        values = request.form
        name = values["email"]
        password = values["pass"]

    return render_template("sign_up")