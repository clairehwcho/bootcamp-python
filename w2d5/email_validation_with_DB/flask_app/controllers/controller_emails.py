from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_email import Email

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['POST'])
def create():
    if not Email.validator(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template("success.html", all_emails=emails)

@app.route('/destroy/<int:id>')
def destroy(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/success')

