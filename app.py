#Oceanofpeople app - A simple crud app that manage data of employees, student, workers along with names, email, number and a photo.
#Technologies Used in this Project - Flask, sqlite3, 

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# Function to insert data into the database
def insert_data(name, number, email, work, department, gender, photo):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users (name, number, email, work, department, gender, photo)
                    VALUES (?, ?, ?, ?, ?, ? ,?)''', (name, number, email, work, department, gender, photo))
    conn.commit()
    conn.close()

# Home route to display the form
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle form submission
@app.route('/add', methods=['POST'])
def add_data():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    work = request.form['work']
    department = request.form['department']
    gender = request.form['gender']

    photo = request.files['photo']

    if photo:
        photo.save('static/uploads/' + photo.filename)
        photo_path = 'static/uploads/' + photo.filename
    else:
        photo_path = ''



    insert_data(name, number, email, work, department, gender,)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
