'''
scraping a live website
website name =https://news.ycombinator.com
'''
import requests
from bs4 import BeautifulSoup

website ="https://news.ycombinator.com"

response = requests.get(website)
webpage= response.text
soup = BeautifulSoup(webpage,"html.parser")
articles =soup.find_all(name="a",class_="storylink")
article_txt =[]
article_link =[]
for article_tag in articles:
    text = article_tag.getText()
    article_txt.append(text)
    link =article_tag.get("href")
    article_link.append(link)
article_vote= [int(score.getText().split()[0]) for score in soup.find_all(name ="span",class_='score')]
##############
print(max(article_vote))
max_point=max(article_vote)
max_index = article_vote.index(max_point)
print(f"the Article: {article_txt[max_index]}\nThe Points: {article_vote[max_index]}\nThe Link: {article_link[max_index]}")




