from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "email_validation_schema"

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        result = connectToMySQL (DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for row in results:
                all_users.append( cls(row) )
            return all_users
        return False

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data):
        is_valid = True

        if len(data['email']) < 1:
            flash('field is required')
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']):
            flash('Email is not valid.')
            is_valid = False

        else:
            existing_email = Email.get_one_by_email({'email':data['email']})
            if existing_email:
                flash('Email is already in use')
                is_valid = False

        return is_valid
