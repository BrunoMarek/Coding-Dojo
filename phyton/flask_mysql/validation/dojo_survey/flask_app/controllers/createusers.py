import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User


@app.route('/home/register', methods=['POST'])
def register():
    
    if User.validate_registration(request.form):
        data = {
            'first_name': request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        
        # user=  Use to log in after register (giving int error)
        User.create_user(data)
        # session['user_id'] = user.id
        # session['user_email'] = user.email
        # session['user_first_name'] = user.first_name
        
        return redirect('/madeit')
    
    return redirect('/home')








@app.route('/')
def index():
    User.validate_registration
    users = User.create_user
    return render_template('index.html', users=users)


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])

@app.route('/return', methods=['POST'])
def comeback():
    
    return redirect('/')