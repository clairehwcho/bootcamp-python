from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "recipes_schema"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.pw = data['pw']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            current_user = cls(result[0])
            return current_user
        else:
            return None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        result = connectToMySQL (DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for row in results:
                all_users.append( cls(row) )
            return all_users
        return False

    @staticmethod
    def validate_registration(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash('First name must be at least 2 characters.', 'err_users_first_name')
            is_valid = False

        if len(data['last_name']) < 2:
            flash('Last name must be at least 2 characters.', 'err_users_last_name')
            is_valid = False

        if len(data['email']) < 1:
            flash('field is required', 'err_users_email')
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email format', 'err_users_email')
            is_valid = False

        else:
            existing_email = User.get_one_by_email({'email':data['email']})
            if existing_email:
                flash('Email already in use', 'err_users_email')
                is_valid = False

        if len(data['pw']) < 1:
            flash('field is required', 'err_users_pw')
            is_valid = False

        if len(data['confirm_pw']) < 1:
            flash('field is required', 'err_users_confirm_pw')
            is_valid = False

        elif data['pw'] != data['confirm_pw']:
            flash('Passwords do not match', 'err_users_confirm_pw')
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True

        if len(data['email']) < 1:
            flash('field is required', 'err_users_email_login')
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email', 'err_users_email_login')
            is_valid = False

        else:
            existing_email = User.get_one_by_email({'email':data['email']})
            if not existing_email:
                flash('Invalid email', 'err_users_email_login')
                is_valid = False
            #check the hash
            elif not bcrypt.check_password_hash(existing_email.pw,data['pw']):
                flash('Invalid password', 'err_users_pw_login')
                is_valid = False
            else:
                #store the id into session
                session['current_user'] = existing_email.id

        if len(data['pw']) < 1:
            flash('field is required', 'err_users_pw_login')
            is_valid = False

        return is_valid