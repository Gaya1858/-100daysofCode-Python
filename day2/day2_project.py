'''
BMi Calculator
BMI = weight/height^2
'''
'''
weight = float(input("Enter your weight: \n"))
height = float(input("Enter your height: \n"))

bmi =weight/((height/100) **2)
print("You BMI is: ",round(bmi,2)) # floating point number with 2 digits
print("You BMI is: ",round(bmi,0)) # rounded bumber '''

'''
print(8//3) # integer
print(8/3)# float
print(round(8/3)) # rounded to integer 2.666 becomes 3

score =0
height =1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}") # f-string ---- addinf "f" in front of the print matter is very important when you use function f-string
'''
'''
Youe Life in Weeks program
if we live until 90 years old
'''
'''
age = int(input("eneter your age: "))
age_remain =90-age
days = age_remain*365
weeks = age_remain*52
months =age_remain*12
print(f"You have {days} days, {weeks} weeks, and {months} months left")'''
'''
Day2 final project - calaculating tips 

'''
bill_amount = float(input("Enter your total bill\n"))
tip_percent = float(input("Enter the percentage of the tip you wnat to pay\n"))
num_people = int(input("Enter the number of people to split the bill amount\n"))

tip = (bill_amount*tip_percent)/100
ttl = bill_amount+tip
split = ttl/num_people
print(f"The bill amount is: {bill_amount},\nthe tip percentage is: {tip_percent} "
      f"= {tip},\ntotal amount to be paid including tips: {ttl},\n"
      f"total number people to split: {num_people},\nand for each have to pay: {split}.")