from flask import flash
from typing import ClassVar
from flask_app.config.mysqlconnection import connectToMySQL
import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);'

        result = connectToMySQL('survey').query_db(query, data)

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

        connectToMySQL('survey').query_db(query,data)
    
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('survey').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @staticmethod
    def validate_registration(data):

        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # name and last between 2 and 32 char

        if len(data['name']) < 2 or len(data['name']) > 32:
                flash('name should be 2 to 32 characters.')
                is_valid = False
        
        if len(data['comment']) < 2 or len(data['comment']) > 50:
                flash('Last name should be 2 to 32 characters.')
                is_valid = False
        
        if len(data['location']) == 0:
            flash("Please provide a location.")
            is_valid = False
        
        if len(data['language']) == 0:
            flash("Please provide a language.")
            is_valid = False



        
        return is_valid
