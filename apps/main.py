# @author Satyam Mishra

from flask import Blueprint, abort, redirect, render_template, request, url_for
import flask
from apps.packages.pyrebase import *

# Blueprint Configuration adding to main app
main = Blueprint(
    'main', __name__,
)

@main.route("/")
def index():
    '''INDEX PAGE OF WEBSITE (AT websiteName)'''
    try:
        # FETCHING AND INCREMENTING PAGE VISIT COUNT
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        # IF EXCEPTION OCCURED ABORT TO CONNECTION NOT FOUND
        pass

    # RETURN HOME PAGE
    return render_template("main/Life-Overseas---Home.html")




@main.route("/about")
def about():
    '''ABOUT PAGE OF MAIN WEBSITE (AT website/about)'''
    try:
        # FETCHING AND INCREMENTING PAGE VISIT COUNT
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        # IF CONNETION LOST ABORTING TO 502 ERROR
        pass

    # RETURNING ABOUT PAGE TEMPLATE
    return render_template("main/Life-Overseas---About.html")




@main.route("/contact")
def contact():
    '''CONTACT PAGE OF MAIN WEBSITE (AT website/contact'''
    try:
        # FETCHING AND INCREMENTING PAGE VISIT COUNT
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    except:
        # IF CONNETION LOST ABORTING TO 502 ERROR
        pass

    # RETURNING CONTACT PAGE TEMPLATE
    return render_template("main/Life-Overseas---Contact.html")




@main.route("/faculty", methods=["GET","POST"])
def faculty():
    # DEFINING QUESTIONS DICT VARIABLE
    questions = dict()
    try:
        # FETCHING AND INCREMENTING PAGE VISIT COUNT
        visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
        realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
        # READING ALL QUESTIONS FROM REALTIME DATABASE
        questions = dict(realtime_db.child("AppData").child("Questions").get().val())
    except:
        # IF CONNETION LOST ABORTING TO 502 ERROR
        pass
    # PASSING QUESTIONS DICT INSIDE DATA DICT VARIBALE
    data= {
        "questions": questions,
    }

    print(questions)
    # IF POST METHOD IS REQUESTED 
    if request.method == "POST":
        # GETTING INPUT QUESTION FROM USER
        values = request.form
        question = values["question"]
        try:
            # SENDING INPUT QUESTION TO REALTIME DATABASE WITH NO ANSWER
            realtime_db.child("AppData").child("Questions").child(question).set("Yet to be answered by our team.")
        except:
            # IF ANY ERROR OCCURED RETURNING TO HOME PAGE OF WEBSITE
            return redirect(url_for('main.index')) 
        else:
            # PASSING MESSAGE IF NO EXCEPTION OCCURED (MEANS QUESTION POSTED)
            flask.flash("Question has been posted.","success")   
    
    # RETURNING FACULTY PAGE TEMPLATE
    return render_template("main/Life-Overseas---Faculty.html",data=data)


