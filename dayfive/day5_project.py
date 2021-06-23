'''
password generating project.
user can choose to have a length of the password from 26 alphabatic letter, 10 integers and 9 other symbols
'''

import random

alphabet_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
int_list =['0','1','2','3','4','5','6','7','8','9']
symbol_list =['!','#','$','%','^','&','*','(',')']

print("Welcome to the password generating program!")
print("user can choose to have a length of the password from 26 alphabatic letter, 10 integers and 9 other symbols")

user_letter = int(input("How many letter do you want in your password?\n"))
user_int = int(input("How many integers do you want in your password?\n"))
user_sym = int(input("How many symbols do you want in your password?\n"))
 #easy level
password =""
for char in range(1,user_letter+1):
    random_char =random.choice(alphabet_list)
    password += random_char
for i in range(1,user_int+1):
    random_int=random.choice(int_list)
    password+=random_int
for i in range(1,user_sym+1):
    random_sym=random.choice(symbol_list)
    password+=random_sym

print("Your password is: "+password)

#hard level

random_hard =random.sample(password,len(password))
password1=""
for i in random_hard:
    password1 +=i
print("Your hard password is: "+password1)
