from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LAGPUdfljjnjr021sdkjhs'

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
        if len(request.form['username']) > 2:
            flash('Message send',category='success')
        else:
            flash('Send error', category='error')

    return render_template('contact.html', title='Feedback', menu=menu)

@app.route("/profile/<username>")
def profile(username):
    if 'userLogger' not in session or session ['userLogger'] != username:
        abort(401)
    return f"User profile: {username}"

@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogger' in session:
        return redirect(url_for('profile', username=session['userLogger']))
    elif request.method == "POST" and request.form['username'] == "fratercula" and request.form['psw'] == "1991":
        session['userLogger'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogger']))
    return render_template('login.html', title='Login', menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Page Not Found', menu=menu), 404

# web server
if __name__ == "__main__":
    app.run(debug=True)


