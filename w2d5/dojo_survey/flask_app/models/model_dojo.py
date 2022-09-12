from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = "dojo_survey_schema"

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, comment) VALUES (%(name)s, %(location)s, %(comment)s);"
        results = connectToMySQL (DATABASE).query_db(query, data)
        return results

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL (DATABASE).query_db(query)
        return Dojo(results[0])

    @staticmethod
    def validator(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.", 'err_users_name')

        if len(dojo['location']) < 1:
            is_valid = False
            flash("Location must be selected.", 'err_users_location')

        if len(dojo['language']) < 1:
            is_valid = False
            flash("Language must be selected.", 'err_users_language')

        if len(dojo['comment']) < 1:
            is_valid = False
            flash("Comment must be selected.", 'err_users_comment')

        return is_valid