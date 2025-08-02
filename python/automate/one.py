from time import sleep
from selenium import webdriver
from selenium import *


driver = webdriver.Safari()
driver.get("https://instagram.com")

username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')

username.send_keys('thebhanushaliboy')

password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/	div[2]/div[1]/div/form/div[3]/div/label/input')

password.send_keys('HobbitBanda')


logbutton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/	div[2]/div[1]/div/form/div[4]')

logbutton.click()


  