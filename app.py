import pyrebase
from flask import Flask, flash, redirect, render_template, request, url_for

name = "Life Overseas"
app = Flask(name)


config = {
  "apiKey": "AIzaSyALZS0dDe0Btyg_K7YFOOnWRNkJxapKMK0",
  "authDomain": "life-overseas.firebaseapp.com",
  "databaseURL": "https://life-overseas-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "life-overseas",
  "storageBucket": "life-overseas.appspot.com",
  "messagingSenderId": "2966303536",
  "appId": "1:2966303536:web:061114482e2d9d4c870ef5",
  "measurementId": "G-D52BSC4QRN"
};
firebase = pyrebase.initialize_app(config)
user_auth = firebase.auth()
realtime_db = firebase.database()




Admin_login = {
    "locked":True,
    "name":"",
    "adminNo":0,
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
                    Admin_login["adminNo"]=ind
                    Admin_login["name"]=name

        except:
            return redirect(url_for("index"))

    return render_template("Admin.html")

@app.route("/admin/panel")
@app.route("/admin/dashboard")
def admin_panel():
    if Admin_login["locked"]==True:
        return redirect(url_for("admin"))
    elif Admin_login["locked"]==False:
        return render_template("Admin-Panel.html",Admin_login)
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

@app.route("/faculty")
def faculty():
    return render_template("Life-Overseas---Faculty.html")


if __name__=="__main__":
    app.run(debug=True)