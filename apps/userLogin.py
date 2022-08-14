from flask import Flask, redirect, render_template, request, url_for
from flask import Blueprint
from flask import current_app as app
import flask
from apps.packages.pyrebase import *


userLogin = Blueprint(
    'userLogin', __name__,
    url_prefix='/user'
)

@userLogin.route("/auth",methods=["GET"])
@userLogin.route("/auth/<status>",methods=["GET"])
def user_auth(status=None):
    try:
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        pass

    return render_template('userAuth.html',status=status)


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

        try:
            auth.create_user_with_email_and_password(email, password)

            return redirect(url_for('userLogin.user_auth'),status='success')
        except:
            return redirect(url_for('userLogin.user_auth',status='error'))
                            

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