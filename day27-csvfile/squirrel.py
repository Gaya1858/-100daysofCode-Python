'''
this program takes Cebtral Park Squirrel census and creates CSV file fur color wise count
from the huge squirrel.csv file
'''

import pandas

data = pandas.read_csv("Squirrel.csv")
fur_data =data["Primary Fur Color"].to_list()
x =0
y=0
z =0
for i in fur_data:
    if(i =="Gray"):
        x +=1
    if(i =="Black"):
        y +=1
    if(i =="Cinnamon"):
        z +=1
fur_color ={'fur_color':['Gray','Black','Cinnamon'],
            'count':[x,y,z]}
data1 =pandas.DataFrame(fur_color)
data1.to_csv("fur-color.csv")