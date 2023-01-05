# @author Satyam Mishra

from flask import abort, redirect, render_template, request, session, url_for
from flask import Blueprint




userLogin = Blueprint(
    'userLogin', __name__,
    url_prefix='/user'
)

@userLogin.route("/auth",methods=["GET"])
@userLogin.route("/auth/<status>",methods=["GET"])
def user_auth(status=None):



    return render_template('userLogin/userAuth.html',status=status)


@userLogin.route("/signin",methods=["POST"])
def user_signin():
    return redirect(url_for('userLogin.user_auth',status='error_login'))
    # if session['email'] != None and session['password'] != None:
    #     email = session['email']
    #     password = session['password']

    #     try:
    #         loged_user = auth.sign_in_with_email_and_password(email,password)
    #     except:
    #         return redirect(url_for('userLogin.user_auth',status='error_login'))
    #     else:
    #         session['localId'] = loged_user['localId']

    #         return redirect(url_for('users.access'))

    # if request.method=="POST":
    #     values = request.form
    #     email = values["email"]
    #     password = values["pass"]
        
    #     try:
    #         valid = auth.get_user_by_email(email)

    #         loged_user = auth.sign_in_with_email_and_password(email,password)
    #     except:
    #         pass
    #     else:
    #         session['email'] = loged_user['email']
    #         session['localId'] = loged_user['localId']

    #         return redirect(url_for('users.access'))
    
            


@userLogin.route("/signup",methods=["POST"])
def user_signup():
    if request.method=="POST":
        values = request.form
        email = values["email"]
        password = values["pass"]

        try:
            print(email)
            print(password)

            

            return redirect(url_for('userLogin.verify_email',status='success'))

        except:
            return redirect(url_for('userLogin.user_auth',status='error_signup'))


                            

@userLogin.route("/forgot_pass",methods=["GET","POST"])
def forgot_pass():

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