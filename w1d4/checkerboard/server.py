from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', row_num=8, column_num=8)

@app.route('/<int:num>')
def checkerboard_one_parameter(num):
    return render_template('index.html', row_num=num, column_num=8)

@app.route('/<int:num1>/<int:num2>')
def checkerboard_two_parameter(num1, num2):
    return render_template('index.html', row_num=num2, column_num=num1)

# @app.route('/<int:num1>/<int:num2>/<string:colorone>/<string:colortwo>')
# def checkerboard_four_parameter(num1, num2, colorone, colortwo):
#     return render_template('index.html', row_num=num2, column_num=num1,color1=colorone, color2=colortwo)



if __name__ == "__main__":
    app.run(debug=True)
