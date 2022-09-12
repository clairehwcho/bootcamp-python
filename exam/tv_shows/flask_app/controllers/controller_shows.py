from flask_app import app, bcrypt
from flask import render_template, request, redirect, session
from flask_app.models.model_show import Show
from flask_app.models.model_user import User

@app.route('/shows')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_shows = Show.get_all_with_users()
    return render_template('shows.html', all_shows = all_shows)

@app.route('/shows/new')
def add_show():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("add_shows.html")

@app.route('/show/create', methods=['POST'])
def save_show():
    # validations
    if not Show.validate_shows(request.form):
        return redirect('/shows/new')
    data = {
        **request.form,
        "user_id": session['user_id']
    }
    Show.save(data)
    return redirect('/shows')

@app.route('/shows/<int:id>')
def show_one_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    current_show = Show.get_one_with_users(data)
    return render_template('show_shows.html', current_show = current_show)


@app.route('/shows/edit/<int:id>')
def display_update_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    current_show = Show.get_one_with_users(data)
    return render_template("edit_shows.html", current_show = current_show)


@app.route('/shows/<int:id>/update', methods=['POST'])
def update_show(id):
    if not Show.validate_shows(request.form):
        return redirect(f'/shows/edit/{id}')
    show_data = {
        **request.form,
        "id" : id,
        "user_id": session['user_id']
    }
    Show.update_one(show_data)
    return redirect('/shows')

@app.route('/shows/<int:id>/delete')
def delete_show(id):
    data = {
        "id" : id,
    }
    Show.delete_one(data)
    return redirect('/shows')