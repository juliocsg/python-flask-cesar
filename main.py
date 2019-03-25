from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import url_for
from flask import redirect

from flask_wtf import CsrfProtect
import forms

app = Flask(__name__)
csrf = CsrfProtect(app)

app.secret_key = 'my_secret_key'
@app.route('/', methods = ['GET', 'POST'])
def index2():
    if 'username' in session:
        username = session['username']
        print(username)
    '''custome_cookie = request.cookies.get('custome_cookies', 'Undefined')
    print(custome_cookie)'''
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
if __name__ == '__main__':
    app.run(debug = True, port=9000)
