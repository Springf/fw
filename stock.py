from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Stock!"

@app.route("/final")
def final():
    return f"Welcome to the destiny of world, {randint(1,100)} Years!"