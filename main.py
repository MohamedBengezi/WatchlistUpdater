from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# Defining webdriver, tradingview url, symbol array, and selenium actionchains
driver = webdriver.Chrome()
URL = "https://www.tradingview.com/chart/DyTqgXAt/"
symbols = []
actions = ActionChains(driver)


# Retrieving tradingview login email and password from info.txt
def get_login_info():
    f = open("info.txt", "r")
    lines = f.readlines()
    username = lines[0]
    password = lines[1]
    return username, password


# Reading symbols from second column of a csv file
def read_from_csv():
    with open("list.csv", "r") as csv_list:
        for line in csv_list:
            symbol = line.split(",", 3)[1].strip("\"")
            if symbol == "Symbol":
                continue
            symbols.append(symbol)
            print(symbol)


# Signing in to tradingview
def sign_in():
    signin = driver.find_element_by_class_name("tv-header__user-menu-button")
    signin.click()
    signin2 = driver.find_element_by_class_name("item-2IihgTnv")
    signin2.click()

    sleep(1)

    signin3 = driver.find_element_by_class_name("js-show-email")
    signin3.click()
    email = driver.find_elements_by_name("username")[0]
    email.send_keys("bengezimohamed@gmail.com")

    passw = driver.find_element_by_name("password")
    passw.send_keys(password)
    signin4 = driver.find_element_by_xpath("//button[@type=\"submit\"]")
    signin4.click()


# Adding each symbol in symbols array to watchlist by pressing Alt + W
def add_to_watchlist():
    for symbol in symbols:
        actions.send_keys(symbol)
        actions.send_keys(Keys.ENTER)
        sleep(1)
        actions.key_down(Keys.ALT).send_keys("w").key_up(Keys.ALT).perform()
        sleep(1)
    actions.perform()


driver.get(URL)
username, password = get_login_info()
read_from_csv()
sign_in()
sleep(2)
add_to_watchlist()
