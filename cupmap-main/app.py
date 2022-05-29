import flask
from flask import Flask, render_template, abort, request, redirect
# from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from werkzeug.security import generate_password_hash, check_password_hash
from data import test_comments, test_location, test_users
import database
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
# auth = HTTPBasicAuth() 

login_manager = LoginManager()

login_manager.init_app(app)


users = {
    "Barbara Middleton": generate_password_hash("barbara"),
    "Elena Kurkova": generate_password_hash("elena")
}

app.secret_key = b'cqbc[5b[]b85m4,w.1,g}(cwj__eg(?d,f'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User():
    def __init__(self, username):
        self.username = username
    
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @classmethod
    def get(cls,username):
        return User(username)

# @auth.verify_password
# def verify_password(username, password):
#     if username in users and \
#             check_password_hash(users.get(username), password):
#         return username

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():

            username = form.username.data
            password = form.password.data

            if username in users and \
                check_password_hash(users.get(username), password):
        # Login and validate the user.
        # user should be an instance of your `User` class
                user = User(username)
                login_user(user)

                flask.flash('Logged in successfully.')

                next = flask.request.args.get('next')
                # is_safe_url should check if the url is safe for redirects.
                # See http://flask.pocoo.org/snippets/62/ for an example.
                if not is_safe_url(next):
                    return flask.abort(400)

                return flask.redirect(next or flask.url_for('feed'))
    return flask.render_template('login.html', form=form)

@app.route("/")
@login_required
def feed():
    username = current_user.username
    return render_template('map.html', userId=True, addNew=True, user=username)

@app.route("/location/<int:location_id>")
@login_required
def place(location_id):
    locations = database.get_locations(location_id)
    return render_template('location.html', userId=True, isMap=True, locations=locations)

@app.route("/login")
def enter():
    return render_template('login.html', moreAbout=True)

@app.route("/rate/<int:location_id>")
@login_required
def rating(location_id):
    location = test_location[location_id]
    return render_template('rate.html', location=location, userId=True, isMap=True)

@app.route("/add_location")
@login_required
def add_new():
    return render_template('add.html', userId=True, isMap=True) 

@app.route("/comments/<int:comment_id>")
@login_required
def comments(comment_id):
    comments = database.get_comments(comment_id)
    return render_template('comments.html', comments=comments, userId=True, isMap=True)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))

@app.route("/profile/<int:user_id>")
@login_required
def my_profile(user_id):
    users = database.get_users(user_id)
    return render_template('profile.html', users=users, userId=True, isMap=True, addNew=True) 

@app.route("/create", methods = ['POST'] )
def create():
    return 'location comment was: ' + request.form['location-comment']

@app.route("/new/<int:comment_id>")
def data(comment_id):
    comments = database.get_comments(comment_id)
    return str(comments)