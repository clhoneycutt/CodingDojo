from flask import Flask, render_template
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    # invoke the connectToMySQL function and pass it the name of the database we're using
    # connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
    mysql = connectToMySQL('mydb')
    all_friends = mysql.query_db("SELECT * FROM users")
    print("Fetched all friends", all_friends)
    return render_template('index.html', friends = all_friends)
    # now, we may invoke the query_db method
    print("all the users", mysql.query_db("SELECT * FROM users;"))
if __name__ == "__main__":
    app.run(debug=True)
    