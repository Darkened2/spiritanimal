from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("/index.html")
    

@app.route('/spiritanimal',methods=["GET","POST"])
@app.route('/spiritanimal.html',methods=["GET","POST"])

def spiritanimal():
    userdata=request.form
    
    pride1=userdata["pride1"]
    problems2=userdata["problems2"]
    Good3=userdata["Good3"]
    Loyalty4=userdata["Loyalty4"]
    Care5=userdata["Care5"]
    support6=userdata["support6"]
    Friends7=userdata["Friends7"]
    scared8=userdata["scared8"]
    total = 0
    
    if pride1 == "Yes":
        total = total +3
    elif pride1 == "No":
        total = total + 2
    elif pride1 == "IDK":
        total = total + 1
    else:
        print("NO answer")
        
    if problems2 == "Yes":
        total = total +3
    elif problems2 == "No":
        total = total + 2
    elif problems2 == "IDK":
        total = total + 1
    else:
        print("NO answer")

    if Good3 == "Yes":
        total = total +3
    elif Good3 == "No":
        total = total + 2
    elif Good3 == "IDK":
        total = total + 1
    else:
        print("NO answer")
    
    if Loyalty4 == "Yes":
        total = total +3
    elif Loyalty4 == "No":
        total = total + 2
    elif Loyalty4 == "IDK":
        total = total + 1
        
    if Care5 == "Yes":
        total = total + 3
    elif Care5 == "No":
        total = total + 2
    elif Care5 == "IDK":
        total = total + 1
        
    if support6 == "Yes":
        total = total +3
    elif support6 == "No":
        total = total + 2
    elif support6 == "IDK":
        total = total + 1
        
    if Friends7 == "Yes":
        total = total +3
    elif Friends7 == "No":
        total = total + 2
    elif Friends7 == "IDK":
        total = total + 1
        
    if scared8 == "Yes":
        total = total +3
    elif scared8 == "No":
        total = total + 2
    elif scared8 == "IDK":
        total = total + 1
    else:
        print("NO answer")
    if total >= 11 and total<=15:
        animal= "lion"
        picture="https://www.indiewire.com/wp-content/uploads/2019/07/Screen-Shot-2019-07-11-at-10.32.46-AM.png?w=780"
    if total >= 5 and total<=10:
        animal= "Rabbit"
        picture= "http://agriculture.vic.gov.au/__data/assets/image/0011/182387/Image-6k-Other-pets-section_white-and-brown-rabbit.jpg"
    if total >= 16 and total<=20:
        animal= "Wolf"
        picture="https://thetorngats.com/site/uploads/2016/04/Wolf_Square.jpg"
    if total >= 21 and total<=24:
        animal= "Tiger"
        picture="https://www.highlandwildlifepark.org.uk/media/1060/15_06_30_amurtiger_male_marty_closeup.jpg"
        
    return render_template("/spiritanimal.html", pride1=pride1,problem2=problems2,Good3=Good3,Loyalty4=Loyalty4,Care5=Care5,support6=support6,Friends7=Friends7,scared8=scared8,total=total,animal=animal,picture=picture)