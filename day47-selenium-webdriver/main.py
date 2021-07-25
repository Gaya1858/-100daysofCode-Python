from selenium import webdriver

chrome_driverPath ='/Users/gaya/Documents/Development/chromedriver'
# driver =webdriver.Chrome(executable_path=chrome_driverPath)
# '''
# we are choosing with chrome browser now. It can aslo work with safari, firefox and all
#  BeautifulSoup is good when webscraping with html, if the web browser uses javascript or
#  angular or frameworks then selenium is best
# '''
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_"
#            "4?crid=36A3MQ82RCXSU&dchild="
#            "1&keywords=instant+pot+Pressure+Cooker&nav_sdd=aps&qid=1627248122&sprefix=instant+pot&sr=8-4") # opens up anew browser window with specified url
# #driver.close()# just close the webpage we opened
#driver.quit() # quit will shutdown entire browser
'''
How to use sel to find and locate particular text on webpage
'''
# price =driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
# driver.quit()
#driver.close()# just close the webpage we opened
driver1 =webdriver.Chrome(executable_path=chrome_driverPath)
driver1.get("https://www.python.org/")
# search_bar=driver1.find_element_bye_nam("q")
# print(search_bar.text)
#driver1.quit()
# xpath
e_time=driver1.find_elements_by_css_selector('.event-widget time')
for time in e_time:
    print(time.text)
e_name=driver1.find_elements_by_css_selector('.event-widget a')
for name in e_name:
    print(name.text)
new_time =[i.text for i in e_time]
new_name =[i.text for i in e_name if i.text != "More"]

new_dict ={i:{j,new_time[i]} for i in range(0,len(new_time)) for j in new_name}
print(new_dict)
driver1.quit()