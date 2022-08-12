# user pages
from flask import Blueprint, redirect, render_template, request, url_for
from flask import current_app as app
from apps.pyrebase import *


main = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static',
)

@main.route("/")
def index():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("Life-Overseas---Home.html")

@main.route("/about")
def about():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("Life-Overseas---About.html")

@main.route("/contact")
def contact():
    visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    realtime_db.child("AppData").child("Website visit count").set(visit_count+1)

    return render_template("Life-Overseas---Contact.html")

@main.route("/faculty",methods=["GET","POST"])
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