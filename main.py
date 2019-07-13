from settings import PORT
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('PORT:', PORT) 
    name="Evelyn"
    return render_template("hello.html", name=name)

@app.route('/sales')
def sales():
    # return "Hello sales"
    return render_template("sales.html", total=42)