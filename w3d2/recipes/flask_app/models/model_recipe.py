from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User
from flask_app import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "recipes_schema"


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = user.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        if result:
            for row in result:
                current_recipe = cls(row)
                user_data = {
                    **row,
                    "created_at": row['users.created_at'],
                    "updated_at": row['users.updated_at'],
                    "id": row['users.id']
                }
                current_user = User(user_data)
                current_recipe.user = current_user
                all_recipes.append(current_recipe)
                print(all_recipes)
            return all_recipes
        return False

    @classmethod
    def get_one_with_users(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = user.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            current_recipe = cls(result[0])
            user_data = {
                **result[0],
                "created_at": result[0]['users.created_at'],
                "updated_at": result[0]['users.updated_at'],
                "id": result[0]['users.id']
            }

            current_recipe.user = User(user_data)
            return current_recipe
        else:
            return None

    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name = %(name)s,description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_add_recipe(data):
        is_valid = True

        if len(data['name']) < 3:
            flash('Name must be at least 3 characters.', 'err_add_recipe_name')
            is_valid = False

        if len(data['description']) < 3:
            flash('Description must be at least 3 characters.', 'err_add_recipe_description')
            is_valid = False

        if len(data['instructions']) < 3:
            flash('Instructions must be at least 3 characters.', 'err_add_recipe_instructions')
            is_valid = False

        if not data['date_cooked']:
            flash('Field is required.', 'err_add_recipe_date_cooked')
            is_valid = False

        return is_valid