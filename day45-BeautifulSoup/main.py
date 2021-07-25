'''
Intro to BS - beautiful soup library
BS is python libraray for pulling data out of html and xml files
'''
from bs4 import BeautifulSoup
import lxml

with open("index.html") as file:
    contents =file.read()
#soup =BeautifulSoup(contents,"html.parser") # you can use
soup =BeautifulSoup(contents,"lxml") # both works in this index.html
# print(soup.title)#<title>Not First Page</title>
# print(soup.title.name) #title
# print(soup.title.string)#Not First Page
# print(soup.text) # all the texts that we put will return by this call
# print(soup.h3.text)# will give heading3 text only.
print(soup.a) # first a tag will be printed
print(type(soup.final_all(name= 'a'))) # all a tag will be printed
print(soup.a.get("href")) # just the first href

