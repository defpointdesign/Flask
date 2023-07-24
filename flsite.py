from flask import Flask
app = Flask(__name__)

# create representation (client request handlers)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return "<h1>about site</h1>"

if __name__ == "__main__":
    app.run(debug=True)

