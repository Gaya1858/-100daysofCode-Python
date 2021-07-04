'''coffee =
{"☕
hot beverage,
Unicode: U+2615 U+FE0F, UTF-8: E2 98 95 EF B8 8F"}
Coffee Machine Program Requirements
1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “​off”​to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make
the drink but print: “​Sorry there is not enough water.”​
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50,
 but they only inserted $0.52 then after counting the coins the program should say “​Sorry that's not enough money.
 Money refunded.​”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the machine
as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.

E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the user selected,
then the ingredients to make the drink should be deducted from the coffee machine resources.
E.g. report before purchasing latte: Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
If latte was their choice of drink.
'''

water =500
milk =500
coffee_powder =250
money =0
machine_status = "off"


def resource_check(order):
    global water,milk,coffee_powder
    if(order == "latte"):
        latte_water = 100
        latte_milk = 100
        latte_powder = 50
        if (water >= latte_water and milk >= latte_milk and coffee_powder >= latte_powder):
            return True
        else:
            return False
    elif (order =="espresso"):
        es_water = 50
        es_milk = 0
        es_powder = 50
        if(water>=es_water and milk >= es_milk and coffee_powder >= es_powder):
            return True
        else:
            return False
    elif (order == "cappuccino"):
        cap_water = 100
        cap_milk = 100
        cap_powder = 50
        if(water >= cap_water and milk >= cap_milk and coffee_powder >= cap_powder):
            return True
        else:
            return False

def resource_report():
    global water,money,milk,coffee_powder
    print("Water: ",water,"ml")
    print("Milk?: ",milk,"ml")
    print("Coffee Powder: ",coffee_powder,"g")
    print("Money: ",money,"$")


def espresso(price):
    global water, milk, coffee_powder,money
    es_water = 50
    es_milk = 0
    es_powder = 50
    water -=es_water
    milk -=es_milk
    coffee_powder -=es_powder
    money +=price
def latte(price):
    global water, milk, coffee_powder,money
    latte_water = 50
    latte_milk = 150
    latte_powder = 50
    water -=latte_water
    milk -=latte_milk
    coffee_powder -=latte_powder
    money +=price

def lcappuccino(price):
    global water, milk, coffee_powder,money
    cap_water = 100
    cap_milk = 100
    cap_powder = 50
    water -=cap_water
    milk -=cap_milk
    coffee_powder -=cap_powder
    money +=price

def user_pay():
   print("Enter the number of coins that you insert, if no coins then enter 0. ")
   dollar = float(input("How many dallar inserted: "))
   quarter =float(input("How many quarters inserted: "))
   dime =float(input("How many dimes inserted: "))
   nickle =float(input("How many nickles inserted: "))
   penny =float(input("How many pennies inserted: "))
   total =(dollar*1.0)+(quarter*0.25)+(dime*0.10)+(nickle*0.05)+(penny*0.01)
   return total

def return_amount(total):
    return total -2.50

def machine_status_on():
    return "on"
def machine_status_off():
    return "off"

print(u"\u2615",end=" ")
print("Gaya's Cofe! ")
print("we serve: espresso/latte/cappuccino")
print("Price is 2.50$")
user_need = input("What would you like?(espresso/latte/cappuccino): ")
if(resource_check(user_need)):
    total =user_pay()
    print()
    if (total >=2.50):
        balance =return_amount(total)
        money-=balance
        if balance >0: print("Here is your balance: ",balance )
        if(user_need == "latte"):
            latte(total)
            print("Here is your Latte "u"\u2615")
        elif(user_need == "espresso"):
            espresso(total)
            print("Here is your Espresso "u"\u2615")
        elif(user_need == "cappuccino"):
            lcappuccino(total)
            print("Here is your Cappuccino "u"\u2615")
        else:
            print("Please enter the correct choice: ")
    else:
        print("You have to pay: ",return_amount(total))
else:
    print("Sorry there is not enough water.")

print()
print("Resource Report: ")
resource_report()


