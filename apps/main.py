# @author Satyam Mishra

from flask import Blueprint, abort, redirect, render_template, request, url_for

# Blueprint Configuration adding to main app
main = Blueprint(
    'main', __name__,
)


@main.route("/")
def index():
    '''INDEX PAGE OF WEBSITE (AT websiteName)'''


    # RETURN HOME PAGE
    return render_template("main/Life-Overseas---Home.html")




@main.route("/about")
def about():
    '''ABOUT PAGE OF MAIN WEBSITE (AT website/about)'''


    # RETURNING ABOUT PAGE TEMPLATE
    return render_template("main/Life-Overseas---About.html")




@main.route("/contact")
def contact():
    '''CONTACT PAGE OF MAIN WEBSITE (AT website/contact'''


    # RETURNING CONTACT PAGE TEMPLATE
    return render_template("main/Life-Overseas---Contact.html")




@main.route("/faculty", methods=["GET","POST"])
def faculty():
    pass
    # # DEFINING QUESTIONS DICT VARIABLE
    # questions = dict()
    # try:
    #     # FETCHING AND INCREMENTING PAGE VISIT COUNT
    #     visit_count = realtime_db.child("AppData").child("Website visit count").get().val()
    #     print(visit_count)
    #     realtime_db.child("AppData").child("Website visit count").set(visit_count+1)
    #     # READING ALL QUESTIONS FROM REALTIME DATABASE
    #     questions = dict(realtime_db.child("AppData").child("Questions").get().val())
    # except:
    #     # IF CONNETION LOST ABORTING TO 502 ERROR
    #     pass
    # # PASSING QUESTIONS DICT INSIDE DATA DICT VARIBALE
    data= {

    }

    # print(questions)
    # # IF POST METHOD IS REQUESTED 
    # if request.method == "POST":
    #     # GETTING INPUT QUESTION FROM USER
    #     values = request.form
    #     question = values["question"]
    #     print(question)
    #     try:
    #         # SENDING INPUT QUESTION TO REALTIME DATABASE WITH NO ANSWER
    #         realtime_db.child("AppData").child("Questions").child(question).set("Yet to be answered by our team.")
    #     except:
    #         # IF ANY ERROR OCCURED RETURNING TO HOME PAGE OF WEBSITE
    #         return redirect(url_for('main.index')) 
    #     else:
    #         # PASSING MESSAGE IF NO EXCEPTION OCCURED (MEANS QUESTION POSTED)
    #         pass    
    # RETURNING FACULTY PAGE TEMPLATE
    return render_template("main/Life-Overseas---Faculty.html", data=data)


