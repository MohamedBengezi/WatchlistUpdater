import csv
import time
from selenium import webdriver
f = open("info.txt", "r")
lines = f.readlines()
username = lines[0]
password = lines[1]
print(username, password)
symbols = []
with open("list.csv", "r") as csv_list:
    for line in csv_list:
        symbol = line.split(",", 3)[1].strip("\"")
        if symbol == "Symbol": continue
        symbols.append(symbol)
        print(symbol)


with open("list.txt", "w") as output:
    [ output.write(symbol+',') for symbol in symbols ]


driver = webdriver.Chrome()
URL = "https://www.tradingview.com/chart/DyTqgXAt/"
driver.get(URL)

signin = driver.find_element_by_class_name("tv-header__user-menu-button")
signin.click()
signin2 = driver.find_element_by_class_name("item-2IihgTnv")
signin2.click()
time.sleep(2)
signin3 = driver.find_element_by_class_name("js-show-email")
signin3.click()

email = driver.find_elements_by_name("username")[0]
email.send_keys("bengezimohamed@gmail.com")

passw= driver.find_element_by_name("password")
passw.send_keys(password)

signin4 = driver.find_element_by_xpath("//button[@type=\"submit\"]")
signin4.click()

time.sleep(2)

settings = driver.find_element_by_xpath("//div[@data-name=\"settings-button\"]")
settings.click()

import_list = driver.find_element_by_xpath("//div[@contains(text(), 'Import list…')]")