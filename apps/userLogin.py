# @author Satyam Mishra

from flask import abort, redirect, render_template, request, session, url_for
from flask import Blueprint
from apps.packages.pyrebase import *
from firebase_admin import credentials,auth
import firebase_admin


cred = credentials.Certificate('adminConfig.json')
firebase_admin = firebase_admin.initialize_app(cred)


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
    if session['email'] != None and session['password'] != None:
        email = session['email']
        password = session['password']

        try:
            loged_user = pb_auth.sign_in_with_email_and_password(email,password)
        except:
            return redirect(url_for('userLogin.user_auth',status='error_login'))
        else:
            session['localId'] = loged_user['localId']

            return redirect(url_for('users.access'))

    if request.method=="POST":
        values = request.form
        email = values["email"]
        password = values["pass"]
        
        try:
            valid = auth.get_user_by_email(email)

            loged_user = pb_auth.sign_in_with_email_and_password(email,password)
        except:
            pass
        else:
            session['email'] = loged_user['email']
            session['localId'] = loged_user['localId']

            return redirect(url_for('users.access'))


@userLogin.route("/signup",methods=["POST"])
def user_signup():
    if request.method=="POST":
        values = request.form
        email = values["email"]
        password = values["pass"]
        try:
            signed_user = pb_auth.create_user_with_email_and_password(email,password)
        except:
            return redirect(url_for('userLogin.user_auth',status='error_signup'))
        else:
            print(signed_user)
            session['email'] = email
            session['password'] = password

            pb_auth.send_email_verification(signed_user['idToken'])

            return redirect(url_for('userLogin.verify_email',status='success'))


                            

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