from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    # invoke the connectToMySQL function and pass it the name of the database we're using
    # connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
    mysql = connectToMySQL('mydb')
    all_friends = mysql.query_db("SELECT * FROM users")
    print("\nAll the friends: \n")
    for friend in all_friends:
        print(friend)
    print("\n")
    return render_template('index.html', friends = all_friends)


@app.route('/create_friend', methods=['POST'])
def creation():
    mysql = connectToMySQL('mydb')
    query = "INSERT INTO users (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }

    new_friend_id = mysql.query_db(query, data)
    print("\nNew Friend's ID: ", new_friend_id, "\n")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    