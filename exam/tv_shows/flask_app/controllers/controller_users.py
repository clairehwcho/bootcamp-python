from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
from flask_app.models.model_show import Show
from flask_app.models.model_user import User

@app.route('/login', methods=['POST'])
def login():
    # validate
    if User.validate_login(request.form):
        current_user = User.get_one_by_email(request.form)
        session['user_id'] = current_user.id
        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/user/create', methods=['POST'])
def register():
    # validations
    if not User.validate_registration(request.form):
        return redirect('/')

    # hashing
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw' : hash_pw
    }

    # create my user
    user_id = User.save(data) # This will return id

    # store current_user in session
    session['user_id'] = user_id
    session['first_name'] = data['first_name']
    session['email'] = data['email']
    return redirect('/shows')