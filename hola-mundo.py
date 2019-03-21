from flask import Flask
app = Flask(__name__)#nuevo objeto
@app.route('/')#wrap o un decorador y la ruta
def index():
    return 'Hola mundo' #funcion
app.run() #Se encarga de ejecutar el servidor en un servidor 5000
