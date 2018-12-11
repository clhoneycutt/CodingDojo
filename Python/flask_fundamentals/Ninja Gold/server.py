from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "SuPeRsEcReTkEy"

@app.route('/')

def index():
    if 'goldamt' not in session:
        session['goldamt'] = 0
    return render_template('index.html')


@app.route('/process_money', methods=['post'])
def process():
    if 'activities' not in session:
        session['activities'] = []
    goldBeforeProcess = session['goldamt']
    
    # Determine building and random win/loss
    if request.form['building'] == 'farm':
        session['goldamt'] += random.randrange(10,21)
    elif request.form['building'] == 'cave':
        session['goldamt'] += random.randrange(5, 11)
    elif request.form['building'] == 'house':
        session['goldamt'] += random.randrange(2, 6)
    elif request.form['building'] == 'casino':
        session['goldamt'] += random.randrange(-50,51)
    
    # Determine variables for activity statement
    difference = session['goldamt'] - goldBeforeProcess
    now = datetime.datetime.now()
    timestamp = now.strftime("%m/%d/%Y %I:%M %p")
    
    # Generate activity statement
    if difference > 0:
        currActivity = f"Earned {difference} golds from {request.form['building']}! ({timestamp})"
        currColor = "win"
    else:
        currActivity = f"Entered a casino and lost {abs(difference)} golds... Ouch.. ({timestamp})"
        currColor = "loss"
    session['activities'].insert(0, {"message": currActivity, "color": currColor})
    return redirect('/')

@app.route('/clear', methods=['post'])
def clear():
    session.clear()
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True) 