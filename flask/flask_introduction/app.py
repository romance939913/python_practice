from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

# runs once before first request, great for initializing apps
@app.before_first_request
def before_first_function():
    print("before_first_request happens once")

# Function runs before each request
@app.before_request
def before_request_function():
    print("before_request is running")

# # erroring out for some reason
# # Function runs after each request
# @app.after_request
# def after_request_function():
#     print("after_request is running")

# routes
@app.route('/')
def home():
    return '<h1>App Home!</h1>'

@app.route('/about')
def about():
    return '<h1>About page</h1>'

@app.route('/item/<int:id>')
def item(id):
    return f'<h1>Item {id}</h1>'