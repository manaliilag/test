from flask import Flask, request

app = Flask(__name__)  # object of Flask


# Lets write hello world using flask and api
@app.route("/")
def hello_world():
    return "Hello World....!"


# another function added
@app.route("/test")
def hello_world2():
    return "Hello World2"


# function calling for get input from url
# http://127.0.0.1:5000/test2?x=datascience
@app.route("/test2")
def input_req1():
    data = request.args.get('x')
    return f"you ask information about {data} ."


# localhost
if __name__ == "__main__":
    app.run(host="0.0.0.0")
