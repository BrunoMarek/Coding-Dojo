import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User


@app.route('/')
def index():
    
    return render_template('login.html')

@app.route('/create_email', methods =['POST'])
def create_email():
    if not User.validate_registration(request.form):
        return redirect('/')
    User.create_user(request.form)
    return redirect('/success')


@app.route('/success')
def emails():
    mail = User.get_all()
    return render_template('success.html', mail=mail)