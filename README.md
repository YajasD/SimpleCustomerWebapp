# SimpleCustomerWebapp
A simple web application that stores a customer's name and an email in a SQL database. Developed using Flask and SQLite3.

To run:
1. Download repo to a folder on your machine.

2. From a terminal navigate to the library folder and run the following command:
sqlite3 customers.db < customers-schema.sql

3. Move up one level to the parent folder and run the following command:
python app.py

3. From your browser, navigate to 0.0.0.0:8080 and use application!


##### Note: This application is currently developed to run locally on your machine using the Flask Development Server. NOT meant to be used in production as it can only handle one request at a time. To be able to use it in production we will need to use a WSGI application server like Waitress/Gunicorn: http://flask.pocoo.org/docs/1.0/tutorial/deploy/
