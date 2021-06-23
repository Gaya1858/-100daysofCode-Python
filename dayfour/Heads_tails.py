'''
Create a game that will play heads or tails
'''

import random

random_coin = random.randint(1,2)
if(random_coin ==1):
    print("Heads!!!")
else:
    print("Tails!!!")
# Lists  data structure . They way of storing and organizing data.

#fruits = ["apple","Orange","banana","grapes"] # example of list. you can add any data type in the list
name = "gaya"
age = 30
height = 5.4
gaya_list = [name,age,height,height] # ordered lists whatever in the 0th position will be always 0th position.
# name is right at the beginning of the list, so it has a offset or shift0, but age is shifted from the beginning by 1
# it is possible to add duplicate items
# list is mutable
print(gaya_list) # output is ['gaya', 30, 5.4]
gaya_list[1] =31
print(gaya_list)
# append function to add at the end

gaya_list.append("fuck") # add item at the end if the item
print(gaya_list)
gaya_list.extend(["Super Girl","summer"])  # if you add without square brackets then it will store each letter as a list
print(gaya_list)#['gaya', 31, 5.4, 5.4, 'Super Girl']
# split string method

alpha_list=['Batman', 'Flash', 'Wonder Woman','Cyborg', 'Superman']
fruits = ["apple","Orange","banana","grapes"]
choices=random.choices(alpha_list,k=7) # creates choices of 7 and duplicates are there as the length is only 5
print(choices)

sample= random.sample(alpha_list,k=3) # it will add duplicates as k shouldn't be greater than the sample population
print(sample)
added_list =[alpha_list,fruits]

# Treasure map
row1 =[" "," "," "]
row2 =[" "," "," "]
row3 =[" "," "," "]