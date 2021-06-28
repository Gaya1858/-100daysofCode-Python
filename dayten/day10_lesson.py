'''
Functions and output
multiple outputs

'''

def sum_of_two(x,y):
    return x+y

#num1 = int(input("Please enter a first number to add: "))
#num2 = int(input("Please enter the second number to add: "))

#print("Sum is: ",sum_of_two(num1,num2))

def format_name(f_name,l_name):
    if(f_name == "" or l_name == ""):
        return "you didn't provide proper names"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title( )
    return f"Result: {formated_f_name} {formated_l_name}"

vel = (format_name("gaya","GAYA"))
#print(vel)

'''
Days in a month calculation. Given year and month, 
the program will calculate the days in a month (whether it is leap or not)
'''
def leap_check(year):
    if(year%400 ==0):
        return True
    elif (year%100 ==0):
        if(year%4 ==0):
            return True
        else:
            return False
    else:
        return False

def month_check(month,year):
    if(month >13 or month<0):
        return " invalid Month"
    result = leap_check(year)
    days =[31,28,31,30,31,30,31,31,30,31,30,31]
    x = month - 1
    for i in range(0,len(days)):
        if (result):
            if (x == 1):
               return("The days in the month of Feb are: ", 29, " and ", year, " is a leap year")
            else:
                if (x == i):
                    return("The days in the month are: ", days[i], " and ", year, " is a leap year")

        else:
            if(x ==i):
                return("The days in the month of Feb is: ", days[i], " and ", year, " is not a leap year")



print("This program will return days in a month and whether it is a leap year or not!")
year = int(input("Enter a year: "))
month= int(input("Enter a month in numbers: "))
print(month_check(month,year))

'''
Doc strings

'''
