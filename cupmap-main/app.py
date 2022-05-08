from flask import Flask, render_template, abort, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from data import test_comments, test_location, test_users
import database

app = Flask(__name__)
auth = HTTPBasicAuth() 

users = {
    "Barbara Middleton": generate_password_hash("barbara"),
    "Elena Kurkova": generate_password_hash("elena")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route("/")
@auth.login_required
def feed():
    return render_template('map.html', user=auth.current_user(), userId=True, addNew=True)

@app.route("/location/<int:location_id>")
@auth.login_required
def place(location_id):
    location = test_location[location_id]
    locations = database.get_locations()
    users = database.get_users()
    comments = database.get_comments()
    users_lookup = {}
    for user in users:
        users_lookup[user['Id']] = user
    return render_template('location.html', location=location, user=auth.current_user(), userId=True, isMap=True, locations=locations, users=users_lookup, comments=comments)

@app.route("/login")
def enter():
    return render_template('login.html', moreAbout=True)

@app.route("/rate/<int:location_id>")
@auth.login_required
def rating(location_id):
    location = test_location[location_id]
    return render_template('rate.html', location=location, user=auth.current_user(), userId=True, isMap=True)

@app.route("/add_location")
@auth.login_required
def add_new():
    return render_template('add.html', user=auth.current_user(), userId=True, isMap=True) 

@app.route("/comments/<int:comment_id>")
@auth.login_required
def comments(comment_id):
    comment = test_comments[comment_id]
    return render_template('comments.html', comment=comment, user=auth.current_user(), userId=True, isMap=True)

@app.route("/logout")
def logout():
    return abort(401)

@app.route("/profile/<int:user_id>")
@auth.login_required
def my_profile(user_id):
    users = test_users[user_id]
    return render_template('profile.html', users=users, user=auth.current_user(), userId=True, isMap=True, addNew=True) 

@app.route("/create", methods = ['POST'] )
def create():
    return 'location comment was: ' + request.form['location-comment']

@app.route("/new")
def data():
    
    comments = database.get_comments()
    return str(comments)