from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PW_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "SuPeRsEcReTkEy"

# ======================================
# SUPPORTING FUNCTIONS
# ======================================


# Checks whether the email is already in the database.
# Used during registration process
def check_duplicates(emailAddress):
    mysql = connectToMySQL('loginreg')
    duplicate_query = "SELECT email FROM users;"
    duplicate_check = mysql.query_db(duplicate_query)
    result = False
    for item in duplicate_check:
        if emailAddress in item['email']:
            result = True
    return result

# Used primarily to end session if account is deleted.
def verify_account(id):
    
    # If not logged in, automatic denial / redirect to homepage.
    if not session['logged_in']:
        flash('You must be logged in to view this page', "nav_error")
        return redirect('/')
    
    # Searches database for specific user id
    # Query ==================
    mysql = connectToMySQL('loginreg')
    query = "SELECT id FROM users WHERE id = %(id)s"
    data = {
        'id': id
    }
    results = mysql.query_db(query, data)
    # ========================
    
    # Validation
    if len(results) < 1:
        session.clear()
        return redirect('/')
    if results[0]['id'] == id:
        # Valid account
        return True
    else:
        # Invalid account
        return False

# Verify email / password and allow or deny login.
def login_validation(email, password):
    
    # Searches database for specific email address
    # Query ==================
    mysql = connectToMySQL('loginreg')
    query = "SELECT * FROM users WHERE email = %(email)s"
    data = {'email': email}
    logincheck = mysql.query_db(query,data)
    # ========================
    
    # Check stored pwhash against the entered password 
    if bcrypt.check_password_hash(logincheck[0]["pwhash"], password):
        # If the password is correct, set some session variables
        session['userid'] = logincheck[0]['id']
        session['loginmessage'] = True       
        session['first_name'] = logincheck[0]['first_name']
        session['logged_in'] = True
        # Successful login
        return True
    else:
        # Failed login
        return False

# ======================================
# MAIN ROUTE
# ======================================


@app.route('/')
def index():
    # Set default session variables
    if 'logged_in' not in session:
        session['logged_in'] = False
    session['recentreg'] = False
    return render_template("index.html")

# ======================================
# REGISTRATION
# ======================================


@app.route('/register', methods=['POST'])
def register():
    
    # First name validations
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank!", 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First name must contain at least two letters and contain only letters!")
    
    # Last name validations
    if len(request.form['last_name']) < 1:
        flash("First name cannot be blank!", 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last name must contain at least two letters and contain only letters!")

    # Email validations
    if len(request.form['email-reg']) < 1:
        flash("Email cannot be blank!", 'email-reg')
    elif not EMAIL_REGEX.match(request.form['email-reg']):
        flash("Invalid Email Address!", 'email-reg')
    elif check_duplicates(request.form['email-reg']):
        flash("We encountered a problem.", 'email-reg')

    # Password validations
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
    elif not PW_REGEX.match(request.form['password']):
        flash("Password must be at least 8 characters long and contain letters, numbers and the following: @#$%^&+=", 'password')

    # Password confirmation validations
    if len(request.form['confpassword']) < 1:
        flash("Please re-enter password", 'confpassword')
    elif request.form['confpassword'] != request.form['password']:
        flash("Passwords must match", 'confpassword')

    # If there are any errors, displays them and does not move forward.
    if '_flashes' in session.keys():
        return redirect("/")
    # Successful registration
    else:

        # Displays welcome message on success page.
        session['recentreg'] = True

        # Hashes password
        pwhash = bcrypt.generate_password_hash(request.form['password'])

        # Creates account in the database
        # Query ====================
        mysql = connectToMySQL('loginreg')
        query = "INSERT INTO users (first_name, last_name, email, pwhash, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pwhash)s, NOW());"
        data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email-reg'],
        'pwhash': pwhash,
        }
        mysql.query_db(query, data)
        # =========================
        
        # First time login
        login_validation(request.form['email-reg'], request.form['password'])
        return redirect('/success')

# ======================================
# LOGIN HANDLING
# ======================================


@app.route('/login', methods=['POST'])
def login():

    # Email validations
    if not EMAIL_REGEX.match(request.form['email-login']) or len(request.form['email-login']) < 1:
        flash("Please enter a valid email address", "email-login")
    elif len(request.form['password-login']) < 1:
        flash("We encountered a problem", 'email-login')
    
    # Redirect if there are validation errors.
    if "_flashes" in session:
        return redirect('/')
    
    # Attempts to login if there are no validation errors.
    validated = login_validation(request.form['email-login'], request.form['password-login'])

    # Failed login
    if not validated:
        flash("We encountered a problem1", "email-login")
    # Successful login
    elif validated:
        return redirect('/success')

# ======================================
# SUCCESSFUL LOGIN / REGISTRATION
# ======================================


@app.route('/thewall', methods=['GET'])
def success():
    
    # Logs user out if account is deleted while they have an active session.
    # Rare circumstance in this instance
    if 'userid' in session:
        if verify_account(session['userid']) != True:
            return redirect('/logout')
    
    # Blocks access if user is not logged in.
    if session['logged_in'] != True or 'logged_in' not in session:
        flash('You must be logged in to view this page', "nav_error")
        return redirect('/')
    
    # If the user just completed registration this will alter the messages 
    # displayed on the success page.
    if session['recentreg']:
        session['regmessage'] = True
        session['loginmessage'] = False

    # Selects all users for display.
    # Query =========================
    mysql = connectToMySQL('loginreg')
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    # ===============================
    
    # variable used to locate most recently added account
    length = len(users) - 1
    return render_template('wall.html', users=users, length=length)

# ======================================
# ACCOUNT DELETION
# ======================================

@app.route('/delete', methods=['POST'])
def delete():
    # Defaults this setting.
    if 'recentreg' in session:
        session['recentreg'] = False
    
    # Deletes row from database
    # Query =========================
    mysql = connectToMySQL('LoginReg')
    session['recentreg'] = False
    query = "DELETE FROM users where id = %(id)s"
    data = {'id': request.form['id']}
    mysql.query_db(query, data)
    # ===============================
    return redirect('/success')

# ======================================
# LOGOUT
# ======================================

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)