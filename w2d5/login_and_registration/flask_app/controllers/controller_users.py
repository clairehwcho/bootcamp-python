from flask_app import app, bcrypt
from flask import render_template, request, redirect, session
# This imports the model file
from flask_app.models.model_user import User

@app.route("/")
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dashboard.html')

# Display Route
@app.route('/login', methods=['POST'])
def login():
    # validate
    User.validate_login(request.form)
    return redirect('/')

@app.route('/logout')
def logout():
    del session['user_id']
    return redirect('/')

# Action Route
@app.route('/register', methods=['POST'])
def register():
    # validations
    if not User.validate(request.form):
        return redirect('/')

    # hashing
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw' : hash_pw
    }

    # create my user
    id = User.save(data) # This will return id

    # store user_id in session
    session['user_id'] = id
    return redirect('/dashboard')

# Display Route
@app.route('/user/<int:id>')
def user_show(id):
    return render_template('user_show.html')

# Display Route
@app.route('/user/<int:id>/edit')
def user_edit(id):
    return render_template('user_edit.html')

# Action Route
@app.route('/user/<int:id>/update', methods=['POST'])
def user_update(id):
    return redirect('/')

# Action Route
@app.route('/user/<int:id>/delete')
def user_delete(id):
    return redirect('/')