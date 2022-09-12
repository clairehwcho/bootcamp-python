from flask import render_template, request, redirect, session

from flask_app import app

from flask_app.models.ninja import Ninja

@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    ninjas = Ninja.get_all(data)
    return render_template("dojo_show.html", all_ninjas=ninjas)

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    dojo_id= data["dojo_id"]
    return redirect(f"/dojos/{dojo_id}")