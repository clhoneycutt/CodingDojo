from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "SuPeRsEcReTkEy"


def check_duplicates(emailAddress):
    mysql = connectToMySQL('validation')
    duplicate_query = "SELECT email FROM users;"
    duplicate_check = mysql.query_db(duplicate_query)
    result = False
    for item in duplicate_check:
        if emailAddress in item['email']:
            result = True
    return result



# ====================================
# ROUTES
# ====================================



@app.route('/', methods=['GET'])
def index():
    if 'creation' not in session:
        session['creation'] = True
    return render_template('index.html')



@app.route('/validate_email', methods=['POST'])
def creation():
    mysql = connectToMySQL('validation')
    session['creation'] = True
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    elif check_duplicates(request.form['email']):
        flash("We are unable to add this e-mail address.")
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        query = "INSERT INTO users (email, created_at) VALUES (%(email)s, NOW());"
    
        data = {
        'email': request.form['email'],
        }
    
        email_address = mysql.query_db(query, data)
        return redirect('/success')



@app.route('/success')
def success():
    mysql = connectToMySQL('validation')
    query = "SELECT * FROM users"
    emails = mysql.query_db(query)
    length = (len(emails)) - 1
    
    return render_template('success.html', emails=emails, length=length)



@app.route('/delete', methods=['POST'])
def delete():
    mysql = connectToMySQL('validation')
    session['creation'] = False
    query = "DELETE FROM users where id = %(id)s"
    data = {
        'id': request.form['id']
    }
    removal = mysql.query_db(query, data)
    return redirect('/success')



if __name__ == "__main__":
    app.run(debug=True)
