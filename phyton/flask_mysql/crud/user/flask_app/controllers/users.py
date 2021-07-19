import re
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User


@ app.route('/')
def index():
    users = User.get_all()
    return render_template('read.html', user=users)


@app.route('/users', methods=['GET', 'POST'])
def read_users():
    users = User.get_all()
    return render_template('read.html', user=users)


@app.route('/users/new')
def new_user():
    return render_template('create.html')


@app.route('/users/new/create', methods=['GET', "POST"])
def create_user():
    User.create(request.form)
    return redirect('/users')


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/users')


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        'id': user_id
    }
    user = User.edit_user(data)
    return render_template('edit.html', user=user)


@app.route('/users/<int:user_id>/update', methods = ['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show(user_id):
    data = {
        'id' : user_id
    }
    user = User.show_user(data)
    return render_template('show.html', user=user)
