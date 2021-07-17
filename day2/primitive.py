# Data types
# String
# "Hello" is 5 character word. It has length of 5 character. Also counting from 0.
# Position of H starts 0
'''
print("Hello",[len("Hello")])
#integer
number = 123_456_789 # _ treated as comma in python
number1 = 123_456_789
num2 = number+number1
print(num2)
# float
x = 3.14567
print(round(x, 2))
# boolean
boo = True
print(type(boo))

# extra stuff
num_char = len(input("enter your name: "))
print(type(num_char)) # now num_char is in interger, as it takes the input and stores its length in the variable.

# adding integer characters together.

print("Welcome to the project adding input characters!")
u_input = input("enter a two digit number")
x = int(u_input[0])
y =int(u_input[1])
print("You have entered: "+u_input+ " .The sum of the digits is: ",x+y)'''

# mathematical symbols
# 6/3 - float
# 2 ** 3  - 2 to the power of 3 which is 8
# python follows PEMDAS rule for processing the mathematical signs

print(3/3+3*3-3)

