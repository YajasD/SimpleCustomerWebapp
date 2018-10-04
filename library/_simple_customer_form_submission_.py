from flask import Flask, g, request, render_template
import sqlite3
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

@app.before_request
def before_request():
    g.db = connect_db()    


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('forms/_basic_customer_form_.html')
    elif request.method == 'POST':
        kwargs = {
            'Name': request.form['Name'],
            'Email': request.form['Email'],
            'secret_key': request.form['SECRET_KEY'],
            'submit_value': request.form['submit'],
        }
        nm = request.form['Name']
        em = request.form['Email']

        cursor = g.db.execute("INSERT INTO customers (Name,Email) VALUES (?,?)",(nm, em))


        g.db.commit()
        return render_template(
            'forms/_basic_customer_form_results_.html', **kwargs)
