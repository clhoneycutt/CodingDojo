from flask import Flask
app = Flask(__name__)


@app.route('/')

def index():
    return "<h1>Hello World!</h1>"

@app.route('/dojo')

def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name

@app.route('/repeat/<mult>/<name>')
def repeated(mult, name):
    mult = int(mult)
    return (name + "\n") * mult


if __name__=="__main__":
    app.run(debug=True)