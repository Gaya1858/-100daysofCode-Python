'''
Web scraping for cheeses around the world, origin and description
website: "https://www.thedailymeal.com/travel/cheese-around-the-world-everyone-should-try/slide-14"
'''
from bs4 import BeautifulSoup
import requests
import pandas

web_link = "https://www.thedailymeal.com/travel/cheese-around-the-world-everyone-should-try/slide-14"
response = requests.get(web_link)
web_page = response.text
soup =BeautifulSoup(web_page,"html.parser")
cheese_names =soup.find_all(name ="div", class_="image-title slide-title")
cheese_des =soup.find_all(name ="div", class_="image-description slide-description")
c_name =[]
c_origin =[]
c_description =[]
stri =""
for n in cheese_names:
    name =n.getText()
    y=name.split("(")
    if( len(y)==3):
        c_name.append(y[0:2])
        s =y[2]
        c_origin.append(s[0:-1])
    else:
        c_name.append(y[0])
        s =y[1]
        c_origin.append(s[0:-1])

c_description=[i.getText() for i in cheese_des]

cheese = []
for i in range(0,len(c_name)):
   cheese.append({"cheese_name":c_name[i],
                  "cheese_origin":c_origin[i],"cheese_description":c_description[i]})
   data = pandas.DataFrame(cheese)
   data.to_csv("cheese.csv", index=False)
