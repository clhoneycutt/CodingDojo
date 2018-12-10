from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'fjsdklfnnsdfklsjdfe'



@app.route('/', methods=['get', 'post'])
def index():
    if 'total_visits' in session:
        print('\n','='*50,'\n total_visits exists! Adding 1 to visit count\n','='*50,'\n')
        session['total_visits'] += 1
    else:
        print('\n','='*50,'\n total_visits does not exist in session. Creating now.\n','='*50,'\n')
        session['total_visits'] = 1
    return render_template('index.html', total=session['total_visits'])

@app.route('/double', methods=["post"])
def double():
    session['total_visits'] += 1
    print('\n','='*50,'\n Double Visit!  Adding 1 extra to visit count\n','='*50,'\n')
    return redirect('/')

@app.route('/clear', methods=['post'])
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)