from flask import Flask, render_template
app = Flask(__name__)
@app.route('/user/<name>')
def user(name='Eduardo'):
    age = 15
    my_list = [1,2,3,4, 6, 7, 8, 9, 10]
    return render_template('user.html', name = name, age = age, list = my_list)
if __name__ == "__main__":
    app.run(debug = True, port=9000)
