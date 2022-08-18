from flask import Flask, abort, flash, redirect, render_template, request, url_for
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

    return render_template('userLogin/userAuth.html',status=status)


@userLogin.route("/signin",methods=["POST"])
def user_signin():
    if request.method=="POST":
        values = request.form
        email = values["email"]
        password = values["pass"]

        print(email, password)

        try:
            signed_user = auth.sign_in_with_email_and_password(email,password)

            return redirect(url_for('users.access'))
        except:
            pass



@userLogin.route("/signup",methods=["POST"])
def user_signup():
    if request.method=="POST":
        values = request.form
        email = values["email"]
        password = values["pass"]

        try:
            signed_user = auth.create_user_with_email_and_password(email, password)
            print(signed_user)
            
            auth.send_email_verification(signed_user['idToken'])
            return redirect(url_for('userLogin.verify_email',status='success'))
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

    return render_template("userLogin/forgotPass.html")

@userLogin.route("/verify_email/<status>",methods=["GET","POST"])
def verify_email(status=None):
    if status=='success':
        return render_template('userLogin/verify_email.html',status=status)
    else:
        # for unauthraized access
        abort(401)