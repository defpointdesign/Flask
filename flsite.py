from flask import Flask, render_template
import json
app = Flask(__name__)


menu = ['Instalation', 'First Application', 'Feedback' ]
@app.route("/")
def index():
    return render_template ('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title='About site', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)

