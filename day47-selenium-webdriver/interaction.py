from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driverPath ='/Users/gaya/Documents/Development/chromedriver'

'''
how to intract with thw elements we find. like cliking into sdomething
'''
driver = webdriver.Chrome(chrome_driverPath)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count=driver.find_element_by_css_selector('#articlecount a')
all_portels =driver.find_element_by_link_text("All portals")
#clicking
#all_portels.click()

#typing
typeing = driver.find_element_by_name("search")
typeing.send_keys("Python")
typeing.send_keys(Keys.ENTER)
