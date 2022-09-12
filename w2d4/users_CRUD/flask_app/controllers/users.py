from flask import render_template, request, redirect, session

from flask_app import app

from flask_app.models.user import User

@app.route("/")
def index():
    return redirect("/users/new")

@app.route("/users/new")
def new():
    return render_template("create.html")

@app.route("/create", methods=["POST"])
def create():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect("/users") # Figure out how to redirect to a url with int

@app.route("/users")
def read():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users=users)

@app.route("/users/<int:id>")
def show(id):
    data = {
        "id": id
    }
    one_user = User.get_one(data)
    return render_template("show_user.html", user=one_user)

@app.route("/users/<int:id>/edit")
def edit(id):
    data = {
        "id": id
    }
    one_user = User.get_one(data)
    return render_template("edit_user.html", user=one_user)

@app.route('/users/update',methods=['POST'])
def update():
    data = {
        "id": request.form["id"],
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "email": request.form["email"],
    }
    User.update(data)
    id = data["id"]
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/delete')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/users')