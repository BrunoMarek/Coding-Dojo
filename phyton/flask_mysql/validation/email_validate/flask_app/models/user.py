from flask import flash
from typing import ClassVar
from flask_app.config.mysqlconnection import connectToMySQL
import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO emails (email) VALUES (%(email)s);'

        result = connectToMySQL('mail').query_db(query, data)

        return result

    @classmethod
    def get_users_with_email(cls, data):
        query ="SELECT * FROM emails WHERE email = %(email)s;"

        results = connectToMySQL('mail').query_db(query, data)

        mail = []

        for item in results:
            mail.append(User(item))
        
        return mail

    
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL('mail').query_db(query)
        mails = []
        for mail in results:
            mails.append(cls(mail))
        return mails

    @staticmethod
    def validate_registration(data):

        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        # validate email

        if not email_regex.match(data['email']):
            flash('Please provide a valid email address')
            is_valid = False
        
        #email is not in use
        elif len(User.get_users_with_email({'email': data['email']})) != 0:
            flash('Email already in use')
            is_valid = False

        
        return is_valid
