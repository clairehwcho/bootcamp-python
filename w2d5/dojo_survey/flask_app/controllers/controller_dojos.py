from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.model_dojo import Dojo


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/create/survey', methods=['POST'])
def create_survey():
    if not Dojo.validator(request.form):
        return redirect('/')
    Dojo.save(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    dojo = Dojo.get_last_survey()
    return render_template("result.html", dojo = dojo)
