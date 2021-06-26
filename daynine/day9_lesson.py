''''
Day9 - Dictionaries and list
nesting lists and dictionaries

'''

# dictionaries are key value pair
# unique keys - duplicate keys are not acceptable
# unordered pair
# using hashcode to order the keys.
# you can fetch values based on keys
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''

# write a program that converts their scores to grades
student_scores = {"Harry":81,"Ron":70,"Hermoine":99,"Laya":99,"gaya":91,"Draco":74,"Neville":62}
student_grades ={}
for score in student_scores.keys():
    if(student_scores[score] >=91 and student_scores[score]<=100 ):
        student_grades[score]="Outstanding"
    elif(student_scores[score] >=81 and student_scores[score]<=90 ):
        student_grades[score]="Exceeds Expectation"
    elif (student_scores[score] >= 71 and student_scores[score] <= 80):
        student_grades[score] = "Acceptable"
    elif (student_scores[score] <= 70 ):
        student_grades[score] = "Fail"

#print(student_scores)
#print(student_grades)

'''
Nesting Lists and Dictionaries
key can have value as a pair and also it can have dict as a value
'''
travel_log =[{"country":"France","cities":["Paris", "Lille","Dijon"],"visits":12}]
def add_travel_log(country,visits,cities):
    new_list ={}
    new_list["country"] =country
    new_list["cities"] =cities
    new_list["visits"] =2
    travel_log.append(new_list)

capitals = {"France": "Paris","Germany": "Berlin","India": "New Delhi","America":"Washington DC"}

#travel_log ={"France":["Paris", "Lille","Dijon"],"Germany":["Stuttgart","Frankfurt"]}
#travel_log ={"France":{"cities_visited":["Paris", "Lille","Dijon"],"total_visited":12},
 #            "Germany":{"cities_visited":["Stuttgart","Frankfurt"],"total_visited":5}}
print(travel_log)
add_travel_log("Russia",2,["moscow","Saint Petersburg"])
add_travel_log("Germany",5,["Stuttgart","Frankfurt"])
print(travel_log)

order ={"Started":{1:"salad",2:"Soup"},
        "main":{1:["burger","fries"],2:["steak"]},
        "dessert":{1:["ice cream"],2:[]}}
print("Starter will be: ",order["Started"][1],"\nMain will be: ",order["main"][2][0],
      "\nDessert will be: ",order["dessert"][1][0])
