"""This module does math"""
import os

from flask import Flask
from flask_pymongo import PyMongo
from jinja2 import Template

app = Flask(__name__)

if os.getenv('MONGODB_URI'):
    app.config['MONGO_URI'] = os.getenv('MONGODB_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    """This function says hello"""
    return "Hello, world!"

@app.route('/<int:a>/<op>/<int:b>')
def calc(a, op, b):
    operation = mongo.db.operations.find_one({'name': op})
    if operation:
        result = Template(operation['pattern']).render(a=a, b=b)
        return f"Result: {a} {op} {b} = {result}"
        # return Template(operation['pattern']).render(a=a, b=b)
    #elif op == '+':
    #    return f"Result: {a} {op} {b} = {a + b}"
    else:
        return f"Result: {a} {op} {b} = Unknown operation"

if __name__ == '__main__':
    app.run(debug=True)
