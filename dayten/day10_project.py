'''
Calculator project
project will show the operation and ask user to pick the operation and
start entering numbers to do the operation.
'''
def add(num1,num2):
    sum = num1+num2
    return sum
def multiply(num1,num2):
    sum = num1*num2
    return sum
def subtract(num1, num2):
    return num1-num2

def divide(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        return print(" Can't divide by zero")
def recursive_calc():
    operation = {"+": add,
                 "-": subtract,
                 "*": multiply,
                 "/": divide}

    should_continue = True
    while (should_continue):

        num1 = int(input("Please enter a number: "))
        for i in operation.keys( ):
            print(i)
        sign = input("Please choose an operation: ")

        num2 = int(input("Enter the second number: "))
        calculation = operation[sign]
        answer = calculation(num1, num2)
        print(f"{num1} {sign} {num2} = {answer}")
        choice = input("Do you want to continue the calculation, say 'y' and for new start of calculatin 'a' else 'n'")
        if (choice == "a"):
            recursive_calc( )

        elif (choice == "y"):
             should_continue = True
        else:
            should_continue = False

print("Calculater program!")
recursive_calc()





