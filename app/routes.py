from app import app
from flask import render_template, request
from app.models import model, formopener
from flask import render_template
from flask import request
from app.models import model

@app.route('/') #(The @ sends someone somewhere)
@app.route('/index')
def index():
    user = {"name": "Sophia", 'color': 'blue', 'animal': 'fox'}
    weather = {'temperature': '70', 'cloud': 'cloudy'}
    return render_template("index.html", title = 'Home Page', user = user, weather = weather)
    
@app.route('/sendBreakfast', methods= ['GET', 'POST'])
def handleBreakfast():
    if request.method == 'GET':
        user = {"name": "Sophia", 'color': 'blue', 'animal': 'fox'}
        weather = {'temperature': '70', 'cloud': 'cloudy'}
        return render_template("index.html", title = 'Home Page', user = user, weather = weather)
    else: #For post requests
        userdata = formopener.dict_from(request.form) #This puts form data into a dictionary
        nickname = userdata['nickname'] #The key for this dictionary comes from the name of the corresponding input in the <form> on the html
        breakfast = model.shout(userdata['breakfast'])
        return render_template('results.html', nickname = nickname, breakfast = breakfast)
#app.route creates a route that we can get to in our url. 
#The function decides what that route should lead to
#The function that returns for a route follows right after the route definition

@app.route('/secret' )
def secretSauce():
    return "<h1> You found a secret! </h1>"
    
@app.route('/turn')
def secretTurn():
    return "<h1> You have a taken a turn! </h1>"

@app.route('/track')
def secretTrack():
    return "<h1> You have tracked a trail! </h1>"
    
@app.route('/make')
def secretRoad():
    return "<h1> You have made a road! </h1>"
    
@app.route('/animal')
def secretAnimal():
    return"<h1> List of animals that are awesome! </h1> <ul> <li>fox</li><li>rabbit</li><li>hawk</li>"
    

@app.route('/food')
def food():
    return "Send food."