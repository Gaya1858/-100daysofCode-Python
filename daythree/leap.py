'''
Leap year with conditional statements


year =int(input("enter a year: \n"))

if(year %4 == 0):
    if(year % 100 ==0):
        if (year % 400 == 0):
            print("It is a leap year!")
        else:
            print("It is not a leap year!")
    else:
        print("It is not a leap year!")
else:
    print("It is not a leap year!")
'''
# ticket with photo problem
'''
height = int(input("what is your height?\n"))
age = int(input("What is your age?\n"))
photo = input("Do you wnat a photo? yes or no answer\n")
price =0
if(height >120):
    if(age <12):
        if(photo == "yes"):
            price = 8
            print("Ticket peice is $8")
        else:
            print("Ticket peice is $5")
    elif(age >=12 and age <= 18):
        if (photo == "yes"):
            print("Ticket peice is $10")
        else:
            print("Ticket peice is $7")
    elif (age >=18):
        if (photo == "yes"):
            print("Ticket peice is $15")
        else:
            print("Ticket peice is $12")
else:
    print("You can not ride!")
'''
# pizza hut problem
#small 15
#medium =20
#large = 25
#pepperoni for small =2
#pepperoni for m and l =3
# extra cheese for any size = 1
'''
size = input("please enter the size of pizza you would like\n")
pepp = input("do you need pepperono?\n")
cheese = input("do you need extra cheese?\n")

if(size == "s" or size == "S"):
    if(pepp =="y" and cheese =="y"):
        print("total amount is: ", (15 + 2 + 1))
    elif (pepp == "y" and cheese == "n"):
        print("total amount is: " , (15 + 2))
    elif (pepp == "n" and cheese == "y"):
        print("total amount is: " , (15 + 1))
    else:
        print("total amount is: " ,(15))
elif(size == "m" or size == "M"):
    if(pepp =="y" and cheese =="y"):
        print("total amount is: " ,(20 + 3 + 1))
    elif (pepp == "y" and cheese == "n"):
        print("total amount is: " , (20 + 3))
    elif (pepp == "n" and cheese == "y"):
        print("total amount is: " , (20 + 1))
    else:
        print("total amount is: " , (20))
elif(size == "l" or size == "L"):
    if(pepp =="y" and cheese =="y"):
        print("total amount is: " , (25 + 3 + 1))
    elif (pepp == "y" and cheese == "n"):
        print("total amount is: " , (25 + 3))
    elif (pepp == "n" and cheese == "y"):
        print("total amount is: " , (25 + 1))
    else:
        print("total amount is: " , (25))
'''
size = input("please enter the size of pizza you would like\n")
pepp = input("do you need pepperono?\n")
cheese = input("do you need extra cheese?\n")
bill =0
if(size =="s"):
    bill+=15
elif(size =="m"):
    bill+=20
elif(size == "l"):
    bill+= 25
if(pepp == "y"):
    if(size =="s"):
        bill += 2
    else:
        bill += 3
if(cheese =="y"):
    bill +=1

print(f"Your total bill is: {bill}")
