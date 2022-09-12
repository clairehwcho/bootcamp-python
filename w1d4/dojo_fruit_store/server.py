from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this is my secret key'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(f"Charging {request.form['first_name']} for fruits")
    session['s_qty'] = request.form['strawberry']
    session['r_qty'] = request.form['raspberry']
    session['a_qty'] = request.form['apple']
    session['fname'] = request.form['first_name']
    session['lname'] = request.form['last_name']
    session['stuID'] = request.form['student_id']
    session['item_total'] = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    return redirect('/orderConfirmation')

@app.route('/orderConfirmation')
def orderConfirmation():
    return render_template("checkout.html")

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)