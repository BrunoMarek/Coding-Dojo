import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route('/')
def index():
    
    return redirect('/home')


@app.route('/home')
def signup():

    return render_template('login.html')


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


@app.route('/home/login', methods=['POST'])
def login():
    users = User.get_users_with_email(request.form)

    if len(users) == 0:
        flash('User with the given email doesnt exist')
        return redirect('/')
    
    user = users[0]

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password for the given email is incorrect')
        return redirect('/')
    
    session['user_id'] = user.id
    session['user_email'] = user.email
    session['user_first_name'] = user.first_name

    flash('Login successful')

    return redirect('/madeit')

@app.route('/madeit')
def loggedin():
    if 'user_id' not in session:
        flash('You must be logged in to see it')
        return redirect('/')
    
    return render_template('logged.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/delete')


#delete some tests



@app.route('/delete')
def delete():
    users = User.get_all()
    return render_template('delete.html', users=users)

@app.route('/delete/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/delete')