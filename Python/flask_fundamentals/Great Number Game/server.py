from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key='fdhsjlfkhdkjalshfjkdhaf'



@app.route('/')

def index():
    randNum = random.randrange(0,101)
    if 'showretry' not in session:
        session['showretry'] = 'hide'
        session['showguess'] = 'show'
    
    if 'answer' not in session:
        session['answer'] = randNum
        print(session['answer'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def thisGuess():
    lastGuess = request.form['guess']
    lastGuess = int(lastGuess)
    if lastGuess == session['answer']:
        session['result'] = f"{session['answer']} was the number! You guessed it!"
        session['color'] = "Green"
        session['showretry'], session['showguess'] = session['showguess'], session['showretry']
    elif lastGuess > session['answer']: 
        session['result'] = "Too high!"
        session['color'] = "black"
    elif lastGuess < session['answer']: 
        session['result'] = "Too low!"
        session['color'] = "Red"
    return redirect('/')

@app.route('/clear', methods=['post', 'get'])
def clear():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)