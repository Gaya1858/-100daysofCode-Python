
from flask import Flask
app = Flask(__name__) # __name__ is a special attribute.
print(__name__)

'''
# python Decorators- decorator function is a function that simply runs another function and gives it some additional 
functionality. @syntatic sugar

(you want to add some functionality to each of the class function then the decorator function do thay.)
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
# python Decorators
# @app.route('/')
#
# def hello_world():
#     return 'Hello, World!'
#
# if __name__ =="__main__":
#     app.run()
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
###########################
def calc(calc_function,n1,n2):
    return calc_function(n1,n2)
result =calc(mul,6,9)

def outer_function():
    print("I am outer")
def nested_function():
    print("I am inner")
    return nested_function

inner_func =outer_function()
inner_func()
##############################
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #  Do something before
        function()
        function()
        #do something after and it runs two times
    return wrapper_function
@delay_decorator
def say_hello():
    time.sleep(2)
    print("Hello")
@delay_decorator
def say_bye():
    print("bye")

say_hello()
say_bye()