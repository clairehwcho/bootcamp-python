# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "login_and_registration_schema"

# model the class after the table from our database
class User:
    def __init__( self , data ):
        # Add attributes for every column in our database
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.pw = data['pw']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    # C
    @classmethod
    def save(cls, data):
        # Add all column names and all values
        query = "INSERT INTO users (first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        # Return me the id/row of the new user addd to the db
        user_id = connectToMySQL (DATABASE).query_db(query, data)
        return user_id

    # R
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

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

    # U
    @classmethod
    def update_one(cls, data):
        # Add columns = values for every column that you wish to change into db
        query = "UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['first_name']) < 1:
            flash('field is required', 'err_users_first_name')
            is_valid = False

        if len(data['last_name']) < 1:
            flash('field is required', 'err_users_last_name')
            is_valid = False

        if len(data['email']) < 1:
            flash('field is required', 'err_users_email')
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email', 'err_users_email')
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
                is_valid = False
                flash('Invalid email/password', 'err_users_email_login')
            #check the hash
            elif not bcrypt.check_password_hash(existing_email.pw,data['pw']):
                is_valid = False
                flash('Invalid email/password', 'err_users_email_login')
            else:
                #store the id into session
                session['user_id'] = existing_email.id

        if len(data['pw']) < 1:
            flash('field is required', 'err_users_pw_login')
            is_valid = False

        return is_valid