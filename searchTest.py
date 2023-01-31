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

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
advancedSearch = driver.find_element(by=By.XPATH, value="//span[@title='Розширений пошук']")
advancedSearch.click()
time.sleep(3)
sortDescendingButton = driver.find_element(by=By.XPATH, value="//span[@class='anticon anticon-arrow-up control-sort-arrow']")
sortDescendingButton.click()
time.sleep(3)
wordNameCard = "Школа танців Dream Team"
nameCard = driver.find_element(by=By.XPATH, value="//div[text()='Школа танців Dream Team']").text
assert_that(nameCard).is_equal_to(wordNameCard)
driver.quit()


