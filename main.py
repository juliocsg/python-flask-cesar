from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import url_for
from flask import redirect
from flask import g
from flask_wtf import CsrfProtect
from models import db
from werkzeug.security import generate_password_hash
from models import User
#from flask_environments import Environments
#<input type="hidden" name="csrf_token" value="{{csrf_token()}}"/>-->

import config
import forms
import json

app = Flask(__name__)

#app.config_class.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://multi_cesar:12345@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config.from_object(config)
#app.config.from_object(config)
#app.config.from_pyfile('config.py')
#app.config.from_envvar('SECRET_KEY')
#app.config.from_envvar('SQLALCHEMY_DATABASE_URI')
#app.SECRET_KEY = 'my_secret_key3'
#csrf = CsrfProtect(app)
#Ejecuta antes del request
@app.before_request
def before_request():
    #if 'username' not in session and request.endpoint not in ['index']:
     #   return redirect
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

@app.route('/logout', methods = ['GET','POST'])
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login')) #el url_for obtiene la función
@app.route('/login', methods = ['GET','POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method =='POST' and login_form.validate():
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
    title = "Curso Flask"
    return render_template('login.html', title = title, form = login_form)
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
                    password = generate_password_hash(create_form.password.data))
        db.session.add(user)
        db.session.commit()
        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)
    title_crear= 'Crear usuario'
    return render_template('create.html',title = title_crear, form = create_form)
@app.after_request
def after_request(response):
    #print(g.test)
    print("3")
    return response #Siempre tiene que devolver el response en after_request

if __name__ == '__main__':
    #csrf.init_app(app)
    #csrf.__init__(app)
    '''
    app.run(debug=True, port = 9000)
    '''
    db.init_app(app)
    with app.app_context():
        db.create_all() #crea todas las tablas
        #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'
    app.run(port=9000)
