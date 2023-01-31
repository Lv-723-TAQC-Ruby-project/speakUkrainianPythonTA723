import time
from assertpy import assert_that

from selenium import webdriver
from selenium.webdriver.common.by import By

url="https://speak-ukrainian.org.ua/dev/"
keyWord="American Gymnastics Club"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
searchField =driver.find_element(by=By.XPATH, value="//input[@type='search']")
searchField.send_keys(keyWord)
time.sleep(3)
club=driver.find_element(by=By.XPATH, value="//div[@class='name']").text
assert_that(club).is_equal_to(keyWord)

driver.quit()


