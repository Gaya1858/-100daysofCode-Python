'''
https://flask.palletsprojects.com/en/1.1.x/quickstart/
Web development Framework - Flask
import Falsk from flask package
export environment variable
export FLASK_APP=hello.py
'''
from flask import Flask
app = Flask(__name__) # __name__ is a special attribute.
print(__name__)

'''
# python Decorators- you want to add some functionality to each of the class function then the decorator function do thay.
decorator give additional functionality to the existing function.
also Functions are first-class objects, can be passed around as arguments example below.
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def calc(calc_function,n1,n2):
    return calc_function(n1,n2)
result =calc(mul,6,9)
# function can be returned from another function 
ef outer_function():
    print("I am outer")
    def nested_function():
        print("I am inner")
    return nested_function

inner_func =outer_function()
inner_func() --- this line will do the same thing as nested_function()
# when the user hits up the path '/' -it will show the home page
'''
#python Decorators
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/bye')
def say_bye():
    return "Bye"
if __name__ =="__main__":
    app.run()
