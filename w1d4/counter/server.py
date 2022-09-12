from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "this is a secret key"


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template("index.html")


@app.route('/count_session', methods=['POST'])
def add():
    if request.form['btn'] == "Add 1":
        session['count'] += 1
    elif request.form['btn'] == "Add 2":
        session['count'] += 2
    return redirect('/')



@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
