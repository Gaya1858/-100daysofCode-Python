from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driverPath ='/Users/gaya/Documents/Development/chromedriver'
driver = webdriver.Chrome(chrome_driverPath)
driver.get("https://secure-retreat-92358.herokuapp.com/")
signfn =driver.find_element_by_name("fName")
signfn.send_keys("Gayathri")

signln =driver.find_element_by_name("lName")
signln.send_keys("Kanagaraj")

email =driver.find_element_by_name("email")
email.send_keys("gayathri1858@yahoo.com")

sign_up =driver.find_element_by_css_selector("form button")
sign_up.click()