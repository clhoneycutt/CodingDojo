from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "SuPeRsEcReTkEy"

@app.route('/')

def index():
    if 'goldamt' not in session:
        session['goldamt'] = 0
    return render_template('index.html')


@app.route('/process_money', methods=['post'])
def process():
    farm = request.form['farm']
    print(farm)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)