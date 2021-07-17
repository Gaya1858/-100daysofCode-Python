'''
functions and inputs

'''
import math
def greet(name):
    # name is the parameter and "Gaya is the argument (name is a variable and gaya is the actual value of the var
    print("Hello "+name+"!")
    print("How do you do?")
    print("Isn't the weather nice today?")


#greet("Gaya")

def personal(name,address):
    print("Hello "+name+"!")
    print("You are coming from "+address +".")

#personal(name = "gaya",address="Pittsford") # Keyword argument
'''
Area calculation
one can of paint can cover 5 sq.m of wall
program calculates the cans paint needed for your wall dimension 
'''
def paint_area(length,width):
    area = length*width
    cans = math.ceil((area/5))
    print("you will need ",cans,"cans of paint")

#user_length =int(input("Enter the length of the wall: "))
#user_width = int(input("Enter the width of the wall: "))

#paint_area(user_length,user_width)

'''
Prime number check 
check whether the user entered a prime number or regular number
'''
def prime_check(number):
    for i in range(1, number):
        if(i != 1 and i!= number):
            if(number%i ==0):
                print("The number ",number,"you entered is not a prime number.")
                return
            else:
                print("The number ",number, "you entered is a prime number.")
                return

user_pri = int(input("Enter the number to check whether it is a prime or not: "))

prime_check(user_pri)