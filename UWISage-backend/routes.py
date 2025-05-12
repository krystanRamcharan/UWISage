from app import app 
from flask import jsonify, request, make_response

@app.route("/signup",methods=["POST"])
def signup():
    print("hello")
    return make_response("sign up here",200)


@app.route("/signin",methods=["POST"])
def signin():
    return make_response("sign in here",200)