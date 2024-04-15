#Oceanofpeople app - A simple crud app that manage data of employees, student, workers along with names, email, number and a photo.
#Technologies Used in this Project - Flask, sqlite3, 

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE_FILE = 'data.db'

# Function to connect to the database
def connect_database():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# Function to initialize the database
def initialize_database():
    conn = connect_database()
    cursor = conn.cursor()

    # SQL to create the table if not exists
    sql = """CREATE TABLE IF NOT EXISTS records (
                name TEXT,
                number TEXT,
                email TEXT,
                place TEXT,
                department TEXT,
                marital_status TEXT,
                gender TEXT
            )"""
    cursor.execute(sql)
    conn.commit()
    conn.close()

# Home route to display the form
@app.route('/')
def home():
    initialize_database()
    return render_template('home.html')

# Route to handle form submission
@app.route('/add', methods=['POST'])
def add_data():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    place = request.form['place']
    department = request.form['department']
    gender = request.form['gender']
    marital_status = request.form['marital_status']

    conn = connect_database()
    cursor = conn.cursor()

    # SQL to insert data into the table
    sql = """INSERT INTO records (name, number, email, place, department, gender, marital_status) 
                VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, (name, number, email, place, department, gender, marital_status))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

