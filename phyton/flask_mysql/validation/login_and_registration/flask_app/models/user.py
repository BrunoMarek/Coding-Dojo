from flask import flash
from typing import ClassVar
from flask_app.config.mysqlconnection import connectToMySQL
import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'

        result = connectToMySQL('signup').query_db(query, data)

        return result

    @classmethod
    def get_users_with_email(cls, data):
        query ="SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL('signup').query_db(query, data)

        users = []

        for item in results:
            users.append(User(item))
        
        return users

    @classmethod
    def delete_user(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s;'

        connectToMySQL('signup').query_db(query,data)
    
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('signup').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @staticmethod
    def validate_registration(data):

        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # name and last between 2 and 32 char

        if len(data['first_name']) < 2 or len(data['first_name']) > 32:
                flash('First name should be 2 to 32 characters.')
                is_valid = False
        
        if len(data['last_name']) < 2 or len(data['last_name']) > 50:
                flash('Last name should be 2 to 32 characters.')
                is_valid = False


        # validate email

        if not email_regex.match(data['email']):
            flash('Please provide a valid email address')
            is_valid = False
        
        #email is not in use
        elif len(User.get_users_with_email({'email': data['email']})) != 0:
            flash('Email already in use')
            is_valid = False

        #password min 8 char

        if len(data['password']) < 8:
            flash('Please use a password of at least eight characters')
            is_valid = False

        #password and confirm pass must match

        if data['password'] != data['confirm_password']:
            flash('Please insure password and confirm password match')
            is_valid = False
        
        return is_valid
