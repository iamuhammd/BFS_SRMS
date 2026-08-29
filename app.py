from flask import Flask, render_template
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

@app.route('/login')
def login():
    return render_template('login.html')