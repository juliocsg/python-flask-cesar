from flask import Flask
from flask import render_template
import forms
app = Flask(__name__)
@app.route('/')
def index2():
    comment_form = forms.CommentForm()

    title = "Curso Flask"
    return render_template('index2.html',title = title, form = comment_form)

if __name__ == '__main__':
    app.run(debug = True, port=9000)
