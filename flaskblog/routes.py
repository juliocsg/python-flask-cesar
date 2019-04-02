from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import json
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import url_for
from flask import redirect
from flask import g
from flask_bcrypt import Bcrypt
#from flask.ext.bcrypt import bcrypt
#from flask
from flask_wtf import CsrfProtect
from models import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from models import User

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.before_request
def before_request():
    #if 'username' not in session and request.endpoint not in ['index']:
     #   return redirect
     #request point indica en que dirección quiere entrar
    if 'username' not in session and request.endpoint in ['comment']:
        return redirect(url_for('login'))
    if 'username' in session and request.endpoint in ['login', 'create']:
        return redirect(url_for(''))
    print("1")
    #el g se puede utilizr en varios eventos como son por ejemplo before y after request
    g.test = 'test1'
    #if 'username' not in session:
    #   print(request.endpoint)
    #  print("El usuario necesita login!")
#error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
@app.route('/', methods = ['GET', 'POST'])
def index2():
    variable = g.test
    print(variable)
    if 'username' in session:
        username = session['username']
        print(username)
    print("2")
    #custome_cookie = request.cookies.get('custome_cookies', 'Undefined')
    #print(custome_cookie)
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        #print comment_form.index('username')
        print (comment_form.username.data)
        print (comment_form.email.data)
        print (comment_form.comment.data)
    else:
        print ('Error en el formulario')
    title = "Curso Flask"
    return render_template('index2.html',title = title, form = comment_form)

@app.route('/cookie', methods = ['GET', 'POST'])
def cookie():
    title = 'Coockies'
    response = make_response( render_template('cookies.html', title = title) )
    response.set_cookie('custome_cookie', 'Eduardo')
    return response
@app.route('/ajax-login', methods = ['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    #diccionario de response
    response = { 'status': 200, 'username': username, 'id': 1}
    #transforma en formato json
    return json.dumps(response)
@app.route('/create', methods = ['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        #Proceso de persistencia en la base de datos
        user = User(username = create_form.username.data,
                    email = create_form.email.data,
                    password = bcrypt.generate_password_hash(create_form.password.data))
        db.session.add(user)
        db.session.commit()
        success_message = 'Usuario registrado en la base de datos'
        print(success_message)
        #flash(success_message)
    title_crear= 'Crear usuario'
    return render_template('create.html',title = title_crear, form = create_form)
@app.after_request
def after_request(response):
    #print(g.test)
    print("3")
    return response #Siempre tiene que devolver el response en after_request

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
