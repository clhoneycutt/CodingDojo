from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "SuPeRsEcReTkEy"


@app.route('/')
def index():
    mysql = connectToMySQL('leads')
    query = "SELECT CONCAT(customers.first_name, ' ', customers.last_name) AS cust_name, customers.created_at AS cust_created, COUNT(DISTINCT leads.id) AS num_leads FROM customers LEFT JOIN leads ON customers.id = leads.customer_id GROUP BY customers.id;"
    leads = mysql.query_db(query)
    if 'range' not in session:
        if 'first_date' not in session and 'second_date' not in session:
            first_date = "YYYY-MM-DD"
            second_date = "YYYY-MM-DD"
        return render_template('index.html', leads = leads, first_date = first_date, second_date = second_date)
    else:
        return render_template('index.html', first_date = session['first_date'], second_date = session['second_date'])

@app.route('/rangefinder', methods=['POST'])
def rangefinder():
    mysql = connectToMySQL('leads')
    query = "SELECT CONCAT(customers.first_name, ' ', customers.last_name) AS cust_name, customers.created_at AS cust_created, COUNT(DISTINCT leads.id) AS num_leads FROM customers LEFT JOIN leads ON customers.id = leads.customer_id WHERE leads.created_at BETWEEN %(date_from)s and %(date_to)s GROUP BY customers.id;"
    session['first_date'] = request.form['date_from']
    session['second_date'] = request.form['date_to']
    data = {
        'date_from': request.form['date_from'],
        'date_to': request.form['date_to']
    }
    session['range'] = mysql.query_db(query, data)
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)