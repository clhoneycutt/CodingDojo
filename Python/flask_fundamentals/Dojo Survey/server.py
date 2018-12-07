from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)

@app.route('/', methods=['POST'])

def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print('message received!')
    name = request.form['name']
    dojo = request.form['location']
    favlang = request.form['favlang']
    comments = request.form['comments']
    return redirect('/success')

@app.route('/success', methods=['POST'])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)