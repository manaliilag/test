from flask import Flask, request, render_template, jsonify

app = Flask(__name__)  # object of Flask


# Lets write hello world using flask and api
@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/cal", methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['maths']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'addition':
            add = num1 + num2
            result = F"The Sum of Given Number {num1} + {num2} = {add}"
        elif ops == 'subtraction':
            add = num1 - num2
            result = F"The Subtraction of Given Number {num1} - {num2} = {add}"
        elif ops == 'multiplication':
            add = num1 * num2
            result = F"The Multiplication of Given Number {num1} * {num2} = {add}"
        elif ops == 'division':
            add = num1 / num2
            result = F"The Division of Given Number {num1} / {num2} = {add}"
        elif ops == 'power':
            add = num1 ** num2
            result = F"The Power of Given Number {num1} ** {num2} = {add}"
        else:
            result = "Please enter right operation...!"
        return render_template('results.html', result=result)


# lets do same thing using postman
@app.route("/calculator", methods=['POST'])
def math_ops_postman():
    if request.method == 'POST':
        ops = request.json['maths']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'addition':
            add = num1 + num2
            result = F"The Sum of Given Number {num1} + {num2} = {add}"
        elif ops == 'subtraction':
            add = num1 - num2
            result = F"The Subtraction of Given Number {num1} - {num2} = {add}"
        elif ops == 'multiplication':
            add = num1 * num2
            result = F"The Multiplication of Given Number {num1} * {num2} = {add}"
        elif ops == 'division':
            add = num1 / num2
            result = F"The Division of Given Number {num1} / {num2} = {add}"
        elif ops == 'power':
            add = num1 ** num2
            result = F"The Power of Given Number {num1} ** {num2} = {add}"
        else:
            result = "Please enter right operation...!"
        return jsonify(result)


# # # # _________________________________________________________
# # Lets write hello world using flask and api
# @app.route("/")
# def hello_world():
#     return "Hello World....!"
#
#
# # another function added
# @app.route("/test")
# def hello_world2():
#     return "Hello World2"
#
#
# # function calling for get input from url
# # http://127.0.0.1:5000/test2?x=datascience
# @app.route("/test2")
# def input_req1():
#     data = request.args.get('x') # get is public post is private
#     return f"you ask information about {data} ."
#
# # # # _________________________________________________________


# localhost
if __name__ == "__main__":
    app.run(host="0.0.0.0")
