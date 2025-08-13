from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

DUMMY_EMAIL = "sugan@gmail.com"
DUMMY_PASSWORD = "sugan123"

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
            flash("Login successful", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('layout/login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
