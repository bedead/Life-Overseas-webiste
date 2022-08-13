from flask import redirect, render_template, request, url_for
from flask import Blueprint
from flask import current_app as app
from apps.packages.pyrebase import *


userLogin = Blueprint(
    'userLogin', __name__,
    url_prefix='/user'
)

@userLogin.route("/auth",methods=["GET","POST"])
def user_auth():
    try:
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        pass

    return render_template('userAuth.html')


@userLogin.route("/signin",methods=["POST"])
def user_signin():
    if request.method=="POST":
        values = request.form
        email = values["email"]
        password = values["pass"]

        print(email, password)



@userLogin.route("/signup",methods=["POST"])
def user_signup():
    if request.method=="POST":
        values = request.form
        email = values["email"]
        password = values["pass"]

        print(email, password)


@userLogin.route("/forgot_pass",methods=["GET","POST"])
def forgot_pass():
    try:
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        pass
    if request.method=="POST":
        data = request.form
        email = data['email']
        
        print(email)

    return render_template("forgotPass.html")