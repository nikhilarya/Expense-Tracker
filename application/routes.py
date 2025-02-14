from application import app
from flask import render_template, url_for, redirect,flash, get_flashed_messages
from application.form import UserDataForm

@app.route("/")
def index():
    return render_template('index.html', title = 'index')

@app.route("/add")
def add_expenses():
    form = UserDataForm()
    return render_template('add.html', title = 'add', form= form)



