from selenium import webdriver
from selenium import *


driver = webdriver.Safari()
driver.get("https://google.com")


searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

searchbox.send_keys('selenium documentation')

searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')

searchbutton.click()
