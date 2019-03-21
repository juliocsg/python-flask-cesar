from flask import Flask, render_template
#from flask import render_template
#from flask import render_template
# ,template_folder=prueba_template
app = Flask(__name__ )
#se utiliza signo de interrogación
@app.route('/')
def inicio():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug = True, port = 9000)
