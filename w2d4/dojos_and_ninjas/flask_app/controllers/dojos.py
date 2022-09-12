from flask import render_template, request, redirect, session

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def show_all_dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=dojos)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/ninjas")
def test():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", all_dojos=dojos)