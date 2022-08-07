from flask import Flask, flash, redirect, render_template, request, url_for
from app.connectDb import *

name = "Life Overseas"
app = Flask(name)


Admin_login = {
    "locked":True,
    "name":"",
    'adminNo':0
}

# Admin Login and panel
@app.route("/admin", methods= ["POST","GET"])
def admin():
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
                print("found")
                ind = admin_names.index(name)
                if (password==admin_passwords[ind]):
                    global Admin_login
                    print("ok")
                    Admin_login["locked"]=False
                    Admin_login['adminNo']=ind
                    Admin_login["name"]=name

                    return redirect(url_for("admin_panel"))

        except:
            return redirect(url_for("index"))

    return render_template("Admin.html")

@app.route("/admin/panel")
def admin_panel():
    if Admin_login["locked"]==True:
        return redirect(url_for("admin"))
    elif Admin_login["locked"]==False:
        return render_template("Admin-Panel.html")
    else:
        return redirect(url_for("index"))





# user pages
@app.route("/", methods=["POST","GET"])
def index():
    return render_template("Life-Overseas---Home.html")

@app.route("/about")
def about():
    return render_template("Life-Overseas---About.html")

@app.route("/contact")
def contact():
    return render_template("Life-Overseas---Contact.html")

@app.route("/faculty", methods=["POST","GET"])
def faculty():
    questions= dict()
    try:
        questions = dict(realtime_db.child("AppData").child("Questions").get().val())
    except:
        pass
    if request.method == "POST":
        values = request.form
        question = values["question"]
        realtime_db.child("AppData").child("Questions").child(question).set("Not yet answers by our team.")
        
        return redirect(url_for('faculty'))
        
    return render_template("Life-Overseas---Faculty.html", questions=questions)

