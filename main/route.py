from main import app, bcrypt, login_manager
from main.model import User
from flask_login import login_user, logout_user,current_user, login_required
from flask import url_for, render_template,flash, redirect, request
from main.form import login_form,Registeration
from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = login_form()
    if current_user.is_authenticated:
        return redirect("home")

    if form.validate_on_submit():
      flash(f'Check your uernsme or password {form.password.data}')
            
    else:  
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'You are now logged-in as {user.username}')
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
    return render_template("login.html", form= form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = Registeration()
    if current_user.is_authenticated:
        return redirect("home")

    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data,email = form.email.data ,password= hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', category="success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html')
