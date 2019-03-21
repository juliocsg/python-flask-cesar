from flask import Flask
from flask import render_template

app = Flask(__name__)
#se utiliza signo de interrogación
@app.route('/')
def index():
    return 'Hola mundo'
@app.route('/params/')
@app.route('/params/<name>/<int:num>')
def params(name = 'este es un valor por default', num='nada'):
    return 'El parámetro es: {} {}'.format(name, num)

if __name__ == '__main__':
    app.run(debug = True, port = 9000)
