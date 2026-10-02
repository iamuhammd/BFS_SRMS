from flask import Flask, render_template, request
import sqlite3
DB_PATH = 'db/srms_db.db'

app = Flask(__name__)
 
# @app.route("/")
# def home():
#     return "I AM Muhammad (IAMuhammad)"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template(about.html)

@app.route('/students')
def students():
    return render_template('students.html')

@app.route('/teachers')
def teachers():
    return render_template('teachers.html')

@app.route('/subjects')
def subjects():
    return render_template('subjects.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    query_result = None
    if request.method == 'POST':
        conn = conn.cursor()
        cursor.execute('SELECT COUNT (*) FROM tbl_students')
        query_result = cursor.fetchone()[0]
        conn.close()
    return render_template('login.html', query_result = query_result)