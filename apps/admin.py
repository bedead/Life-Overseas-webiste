# Admin Login and panel
from flask import redirect, render_template, request, url_for
from flask import Blueprint
from flask import current_app as app
from apps.packages.pyrebase import *


# Blueprint Configuration
admin = Blueprint(
    'admin', __name__,
    url_prefix='/admin'
)

Admin_login = {
    "locked":True,
    "name":"",
    'adminNo':0
}

@admin.route("/", methods= ["POST","GET"])
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
                        
                    return redirect(url_for("admin.admin_panel"))
        except:
            return redirect(url_for("main.index"))

    return render_template("Admin.html")

@admin.route("/dashboard")
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
        "all_notification": notifications,
        "adminName":Admin_login["name"]
    }

    if Admin_login["locked"]==True:
        return redirect(url_for("admin.admin_root"))
    elif Admin_login["locked"]==False:
        return render_template("Admin-Panel.html",admin_data=admin_data)
    else:
        return redirect(url_for("main.index"))

def profile_page():
    pass

def admin_logout():
    pass