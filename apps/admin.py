# @author Satyam Mishra
from flask import abort, redirect, render_template, request, session, url_for
from flask import Blueprint
from apps.packages.pyrebase import *


# Blueprint Configuration adding to main app
admin = Blueprint(
    'admin', __name__,
    # adding this dir as /admin prefix 
    url_prefix='/admin'
)

# const parameters for admin login
Admin_login = {
    "locked":True,
    "name":"",
    'adminNo':0
}

# SETTING TWO ROUTES (ONE WITH ERROR MSG AND ONE WITHOUT)
@admin.route("/", methods= ["POST","GET"])
@admin.route("/<errorMsg>", methods= ["POST","GET"])
def admin_root(errorMsg=None):
    '''ADMIN LOGIN PAGE (INDEX AT <website/admin/>)'''
    global Admin_login
    # WAITING FOR METHOD POST
    if request.method == "POST":
        # GETTING FORM DATA FROM HTML PAGE
        values = request.form
        name = values["name"]
        password = values["pass"]
        # TRY - CATCH BLOCK
        try:
            # FETCHING ALL ADMINS_NAMES AND ADMIN_PASSWORD FROM\
            # FIREBASE REALTIME DATABASE 
            admins_name = dict(realtime_db.child("Data").child("Name").get().val())
            admin_names = list(admins_name.values())
            admin_pass = dict(realtime_db.child("Data").child("Password").get().val())
            admin_passwords = list(admin_pass.values())
        except:
            # ABORTING TO CONNECTION ERROR IF DATA NOT FETCHED
            pass
        else:
            # IF INPUT NAME IN ALL ADMIN_NAME
            if (name in admin_names):
                # GETTING ADMIN_NO
                ind = admin_names.index(name)
                # MATCHING PASSWORD WITH THAT ADMINS PASSWORD
                if (password==admin_passwords[ind]):
                    # CHANGING admin_login DATA
                    Admin_login["locked"]=False
                    Admin_login['adminNo']=ind
                    Admin_login["name"]=name
                    
                    # RETURNING TO ADMIN DASHBOARD PAGE
                    return redirect(url_for("admin.admin_panel"))
                # IF PASSWORD NOT FOUND RETURNING WITH ERROR MESSEAGE
                else:
                    return redirect(url_for('admin.admin_root',errorMsg = 'wrong password entered'))
            # IF ADMIN NAME NOT FOUND RETURNING WITH ERROR MESSEAGE
            else:
                return redirect(url_for('admin.admin_root', errorMsg = 'admin name not found'))

    return render_template("admin/Admin.html")




@admin.route("/dashboard")
def admin_panel():
    '''ADMIN DASHBOARD PAGE (INDEX AT website/admin/dashboard)'''
    # INCREMENING WEBSITE VISITS COUNT BY 1
    # AND SAVING DATA IN FIREBASE REALTIME DATABASE
    try:
        # CONNECTING TO FIREBASE REALTIME DATABASE TO FETCH STATS DATA
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        total_users = realtime_db.child("AppData").child("Total users").get().val()
        daily_login = realtime_db.child("AppData").child("Daily logins").get().val()
        notification_count = realtime_db.child("AppData").child("Notification count").get().val()

        notifications = dict()
    except:
        # ABORTING TO CONNECTION ERROR IF DATA NOT FETCHED
        pass    
    # CREATING DATA DICT TO PASS TO HTML TEMPLATE
    admin_data = {
        "visits": visit_count,
        "users": total_users,
        "notification_count": notification_count,
        "daily_login": daily_login,
        "all_notification": notifications,
        "adminName":Admin_login["name"]
    }

    # IF ROUTE ACCESSED WITHOUT LOGIN THEN
    # admin_login IS LOCKED 
    # RETURN BACK TO ADMIN LOGIN PAGE
    if Admin_login["locked"]==True:
        return redirect(url_for("admin.admin_root"))
    # IF admin_login IS NOT LOCKED THEN
    # RERURNING DASHBOARD TEMPLATE WITH ADMIN DATA
    elif Admin_login["locked"]==False:
        return render_template("admin/Admin-Panel.html",admin_data=admin_data)
    # ELSE
    # RETURN BACK TO WEBSITE HOME PAGE
    else:
        return redirect(url_for("main.index"))




@admin.route("/dashboard/profile", methods= ["POST","GET"])
def profile_page():
    '''ADMIN PROFILE PAGE (INDEX AT website/admin/dashboard/profile)'''
    pass




@admin.route("/logout", methods= ["POST"])
def admin_logout():
    '''ROUTE CALLED WHEN LOGOUT BUTTON IS PRESSED'''
    pass
        



@admin.route("/dashboard/forms", methods= ["POST","GET"])
def forms():
    '''ALL ANSWERING FORMS (INDEX AT website/admin/dashboard/forms)'''
    pass



