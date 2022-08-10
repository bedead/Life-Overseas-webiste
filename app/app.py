from flask import Flask, flash, redirect, render_template, request, url_for
from app.connectDb import *

name = "Life Overseas"
app = Flask(name)
app.secret_key = 'jhsd]e[3984764.573kjs4a1jkrjg876}][}[[.&6s'

Admin_login = {
    "locked":True,
    "name":"",
    'adminNo':0
}
# Admin Login and panel
@app.route("/admin", methods= ["POST","GET"])
def admin_root():
    if request.method == "POST":
        values = request.form
        name = values["name"]
        password = values["pass"]
        try:
            admins_name = dict(realtime_db.child("Data").child("Name").get().val())
            admin_names = list(admins_name.values())
            admin_pass = dict(realtime_db.child("Data").child("Password").get().val())
            admin_passwords = list(admin_pass.values())
            if (name in admin_names):
                ind = admin_names.index(name)
                if (password==admin_passwords[ind]):
                    global Admin_login
                    Admin_login["locked"]=False
                    Admin_login['adminNo']=ind
                    Admin_login["name"]=name
                        
                    return redirect(url_for("admin_panel"))
        except:
            return redirect(url_for("index"))

    return render_template("Admin.html")

@app.route("/admin/dashboard")
def admin_panel():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    total_users = realtime_db.child("AppData").child("Total users").get().val()
    daily_login = realtime_db.child("AppData").child("Daily logins").get().val()
    notification_count = realtime_db.child("AppData").child("Notification count").get().val()
    notifications = {

    }

    admin_data = {
        "visits": visit_count,
        "users": total_users,
        "notification_count": notification_count,
        "daily_login": daily_login,
        "all_notification": notifications
    }

    if Admin_login["locked"]==True:
        return redirect(url_for("admin_root"))
    elif Admin_login["locked"]==False:
        return render_template("Admin-Panel.html",admin_data=admin_data)
    else:
        return redirect(url_for("index"))





# user pages
@app.route("/")
def index():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("Life-Overseas---Home.html")

@app.route("/about")
def about():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("Life-Overseas---About.html")

@app.route("/contact")
def contact():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("Life-Overseas---Contact.html")

@app.route("/faculty",methods=["GET","POST"])
def faculty():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    questions = dict()
    try:
        questions = dict(realtime_db.child("AppData").child("Questions").get().val())
    except:
        pass
    data= {
        "questions": questions,
    }
    if request.method == "POST":
        values = request.form
        question = values["question"]
        try:
            realtime_db.child("AppData").child("Questions").child(question).set("Yet to be answered by our team.")
        except:
            return redirect(url_for('index'))    
        
    return render_template("Life-Overseas---Faculty.html",data=data)





@app.route("/user/signin",methods=["GET","POST"])
def user_login():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("Login page")

@app.route("/user/signup",methods=["GET","POST"])
def user_login():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("sign up")