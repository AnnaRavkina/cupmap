from flask import Flask, render_template
from data import test_comments, comment1

app = Flask(__name__)

@app.route("/")
def feed():
    return render_template('map.html')

@app.route("/location")
def place():
    return render_template('location.html', comments=test_comments)

@app.route("/login")
def enter():
    return render_template('login.html')

@app.route("/rate")
def rating():
    return render_template('rate.html')

@app.route("/add_location")
def add_new():
    return render_template('add.html')

@app.route("/comments/<int:comment_id>")
def comments(comment_id):
    comment = test_comments[comment_id]
    return render_template('comments.html', comment=comment)