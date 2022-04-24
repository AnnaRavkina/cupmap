from flask import Flask, render_template
from data import test_comments, test_location

app = Flask(__name__)

@app.route("/")
def feed():
    return render_template('map.html')

@app.route("/location/<int:location_id>")
def place(location_id):
    location = test_location[location_id]
    return render_template('location.html', comments=test_comments, location=test_location)

@app.route("/login")
def enter():
    return render_template('login.html')

@app.route("/rate/<int:location_id>")
def rating(location_id):
    location = test_location[location_id]
    return render_template('rate.html', location=test_location)

@app.route("/add_location")
def add_new():
    return render_template('add.html') 

@app.route("/comments/<int:comment_id>")
def comments(comment_id):
    comment = test_comments[comment_id]
    return render_template('comments.html', comment=comment)