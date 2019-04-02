from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hola mundo'
@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parámetro')
    param_dos = request.args.get('params2', 'no contiene este parámetro')
    return 'El parámetro es {} {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port = 9000)
