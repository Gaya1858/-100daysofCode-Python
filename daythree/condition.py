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
'''
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
    print("The number you entered is add number")'''
# BMI calculator problem
# if the BMI is below 18, you are underweight
# if your BMI is 18 to 23 then you are normal weight
#if your BMI is more then 23 then you are over weight

user_h = float(input("enter your height\n"))
user_w =float(input("enter your weight\n"))
bmi = round((user_w/(user_h**2)))
print(user_h,user_w,bmi)
string1 = "\033[1m" + "underweight" + "\033[0m"
string2 = "\033[1m" + "normalweight" + "\033[0m"
string3 = "\033[1m" + "overweight" + "\033[0m"
string4 = "\033[1m" + "obese" + "\033[0m"
string5 = "\033[1m" + "should check with doctor immediately" + "\033[0m"
if(bmi < 18.5):
    print("You are "+string1+"!\n")
elif(bmi<25):
    print("You are " + string2 + "!\n")
elif (bmi < 30):
    print("You are " + string3 + "!\n")

elif (bmi < 35):
    print("You are " + string4 + "!\n")
else:
    print("you "+string5+"!\n")