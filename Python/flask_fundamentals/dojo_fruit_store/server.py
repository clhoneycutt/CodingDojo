from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    total = strawberry + raspberry + apple
    
    now = datetime.datetime.now()
    ordered_at = now.strftime("%m-%d-%Y" + ' at ' + "%-I:%M %p")

    print(request.form)
    return render_template("checkout.html", total=total, ordered_at=ordered_at)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    