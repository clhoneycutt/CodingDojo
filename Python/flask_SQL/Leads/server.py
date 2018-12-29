from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('leads')
    leads = mysql.query_db("SELECT CONCAT(customers.first_name, ' ', customers.last_name) AS cust_name, customers.created_at AS cust_created, COUNT(DISTINCT leads.id) AS num_leads FROM customers LEFT JOIN leads ON customers.id = leads.customer_id GROUP BY customers.id;")
    print(leads)
    return render_template('index.html', leads = leads)




if __name__ == "__main__":
    app.run(debug=True)