'''
Conditional statements day3
'''
'''
user_height = int(input("enter your height in cm: \n"))
height = 120
if user_height >height:
    print("you can ride rollercoaster!")
else:
    print("Please grow to ride rollercoaster!")'''
# introduction to modulo

user_num = int(input("enter a number: \n"))
if(user_num%2 ==0):
    print("The number you entered is even!")
    if(user_num%50 == 0):
        x =int(user_num/5)
        print("you entered number that can be divide by 5,10,25 and 50!")
    elif(user_num>50 and user_num% 50 >0):
        print("the number is above 50!")
    else:
        print("the number is below 50!")
else:
    print("The number you entered is add number")