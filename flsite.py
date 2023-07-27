from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu =[{"name": "Installation", "url": "install-flask"},
       {"name": "First Application", "url": "first-app"},
       {"name": "Feedback", "url": "contact"}]



@app.route("/")
def index():
    return render_template ('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title='About site', menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    # checking request POST
    if request.method == 'POST':
        print(request.form['username'])
    return render_template('contact.html', title='Feedback', menu=menu)

# web server
if __name__ == "__main__":
    app.run(debug=True)


