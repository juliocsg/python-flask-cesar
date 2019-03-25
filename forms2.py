from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import validators

def length_honeypot(form,field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacío.')

class LoginForm(Form):
    username = StringField('Username',
    [
        validators.Required(message = 'El username es requerido'),
        validators.length(min=4, max=25, message='Ingrese un username válido!')
    ])
    password = PasswordField('Password',
    [
        validators.required(message = 'El password es requerido')
    ])
