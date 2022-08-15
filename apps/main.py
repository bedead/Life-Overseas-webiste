# user pages
from flask import Blueprint, redirect, render_template, request, url_for
from flask import current_app as app
from apps.packages.pyrebase import *


main = Blueprint(
    'main', __name__,
)

@main.route("/")
def index():
    try:
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        pass

    return render_template("main/Life-Overseas---Home.html")

@main.route("/about")
def about():
    try:
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        pass

    return render_template("main/Life-Overseas---About.html")

@main.route("/contact")
def contact():
    try:
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        pass

    return render_template("main/Life-Overseas---Contact.html")

@main.route("/faculty", methods=["GET","POST"])
def faculty():
    questions = dict()
    try:
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
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
            return redirect(url_for('main.index'))    
        
    return render_template("main/Life-Overseas---Faculty.html",data=data)