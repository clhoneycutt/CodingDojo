from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Thiswillbesecretinproduction'

# Index route to the Homepage.
@app.route('/')
def index():
    return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# handle POST data once, creating a session
# redirect to where it's being handled so it doesn't have to reload every time, giving the user an alert.
@app.route('/users', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    print("\n","="*50,"\n\n User created: ", session['name'], " / ", session['email'], "\n\n", "="*50, "\n")
    return redirect('/show')

# route being used to render the webpage.
# separating the functions into separate routes creates a better user experience.
@app.route('/show')
def show_user():
    return render_template('user.html')


if __name__=="__main__":
    # run our server
    app.run(debug=True) 


# Other helpful tips

# Checking if session['name'] exists.
# if 'name' in session:
#     print('name exists!')
# else:
#     print("key 'name' does NOT exist")

# Clearing session
# session.clear()