from flask_app import app, bcrypt
from flask import render_template, request, redirect, session
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User

@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_recipes = Recipe.get_all_with_users()
    return render_template('recipes.html', all_recipes = all_recipes)

@app.route('/recipes/new')
def add_recipe():
    return render_template("add_recipe.html")

@app.route('/recipe/create', methods=['POST'])
def save_recipe():
    # validations
    if not Recipe.validate_add_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        "user_id": session['user_id']
    }
    Recipe.save(data)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    data = {
        "id": id
    }
    current_recipe = Recipe.get_one_with_user(data)
    return render_template('show_recipe.html', current_recipe = current_recipe)


@app.route('/recipes/<int:id>/update')
def display_update_recipe(id):
    data = {
        "id": id
    }
    current_recipe = Recipe.get_one_with_users(data)
    return render_template("edit_recipe.html", current_recipe = current_recipe)


@app.route('/recipe/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if not Recipe.validate_add_recipe(request.form):
        return redirect(f'/recipes/{id}/update')
    recipe_data = {
        **request.form,
        "id" : id,
        "user_id": session['user_id']
    }
    Recipe.update_one(recipe_data)
    return redirect('/recipes')

@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    data = {
        "id" : id,
    }
    Recipe.delete_one(data)
    return redirect('/recipes')