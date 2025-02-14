from application import app
from flask import render_template, url_for, redirect,flash, get_flashed_messages
from application.form import UserDataForm

@app.route("/")
def index():
    return render_template('index.html', title = 'index')

@app.route("/add", methods = ["GET", "POST"])
def add_expenses():
    form = UserDataForm()
    if form.validate_on_submit():
        ##m will make entry to database
        flash("Successful entry", 'success')
        return redirect(url_for('index'))


    return render_template('add.html', title = 'add', form= form)



