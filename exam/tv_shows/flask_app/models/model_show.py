from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User
from flask_app import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "tv_shows_schema"


class Show:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO shows (title, network, release_date, description, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_shows = []
        for row in result:
            all_shows.append( cls(row) )
        return all_shows

    @classmethod
    def get_one_with_users(cls, data):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id WHERE shows.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            current_show = cls(result[0])
            user_data = {
                **result[0],
                "created_at" : result[0]['users.created_at'],
                "updated_at" : result[0]['users.updated_at'],
                "id" : result[0]['users.id']
            }
            current_show.user = User(user_data)
            return current_show
        else:
            return None

    @classmethod
    def update_one(cls, data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_shows(data):
        is_valid = True

        if len(data['title']) < 3:
            flash('Title must be at least 3 characters.', 'err_add_show_title')
            is_valid = False

        if len(data['network']) < 3:
            flash('Network must be at least 3 characters.', 'err_add_show_network')
            is_valid = False

        if not data['release_date']:
            flash('Field is required.', 'err_add_show_release_date')
            is_valid = False

        if len(data['description']) < 3:
            flash('Description must be at least 3 characters.', 'err_add_show_description')
            is_valid = False

        return is_valid