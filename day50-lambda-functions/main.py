'''
A Lambda funstion is a small anonymous(unknown) function
A lambda function can take any number of arguments,but can only have one expression.
syntax : lambda arguments: expression

why user lambda?
the power of lambda is better shown when you use them as an anonymous function
inside another function

Say you have a function definition that takes one argument, and that
argument will ne multiplied with an unknown number;

def myfunc(n):
    return lambda a: a*n
'''
import math

y =lambda x:x*x
print(y(5))

new = lambda a :a**2
print(new(5))

def myfunc(n):
    return lambda a,b : (a**b) * n

mydoubler = myfunc(2)

print(mydoubler(2,5))

# map()
# map is a builtin function andThe map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# syntax = map(function, iterables)
#
# function	Required. The function to execute for each item
# iterable	Required. A sequence, collection or an iterator object.
#             You can send as many iterables as you like,
#             just make sure the function has one parameter for each iterable.
#

li =[1,2,3,4,5,6,7]

# ne_list =list(map(new,li))
# print(ne_list)
new_list = list(map(lambda a:math.sqrt(a),li))
print(new_list)


