from flask_app import app
from flask import render_template, request, redirect, session

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/recipes')
    return render_template("index.html")

