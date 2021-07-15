'''
csv - comma seprated value
It is an built library
data that fits into to the table
'''
#todo - CSV
'''
pandas libraray is used to manipulate large sets data and analysis the data in tabular form.
It is not a built in module and you have install it to use it

two main datastructures in pandas 
1.dataframe = can be a google sheet, table or spread sheet. table will be created based on the data label. if the columns
                are just numeric values then it will store it as numeric values as well string and other objects
2. series = when you select a column from the table for particular data label like day or temp. it will return its column details one by one 


'''
# import csv
# #
# new_lists =[]
# with open("weather-data.csv")as file1:
#     data=csv.reader(file1)
#     print(data)
#     for row in data:
#         if(row[1] != "temp"):
#             new_lists.append(int(row[1]))
#
# print(new_lists)

import pandas

data = pandas.read_csv("weather-data.csv") # data type is <class 'pandas.core.frame.DataFrame'>

data_day = data.day # data)temp  type is <class 'pandas.core.series.Series'>
print((data_day))
'''
output of series is below
0       Monday
1      Tuesday
2    Wednesday
3     Thursday
4       Friday
5     Saturday
6       Sunday
'''
data_day_list =data_day.to_list() # you can make a list
print((data_day_list))
'''
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
'''
# we can also convert dataframs to dictionaries

data_dict = data.to_dict()
print(data_dict)
'''
{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 
'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 
'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
'''
data_d = pandas.DataFrame(data_dict)
print(data_d.temp.mean())
# temp = data_d["temp"]
# print(temp)
num =0
