import time

from selenium import webdriver
from selenium.webdriver.common.by import By
clubName="Jerome IT School"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://speak-ukrainian.org.ua/dev/")
search =driver.find_element(by=By.XPATH, value='//*[@id="rc_select_0"]')
search.send_keys(clubName)
time.sleep(10)
club = driver.find_element(by=By.XPATH, value='//*[@id="root"]/section/section/main/section/section/main/div/div/div/div/div[1]/div[2]').text

email = "admin@gmail.com"
password = "1234567"
driver.get("https://speak-ukrainian.org.ua/dev/")
addClub = driver.find_element(by=By.XPATH, value='//*[@id="root"]/section/header/div[3]/button')
addClub.click()
time.sleep(3)
emailField = driver.find_element(by=By.XPATH, value='//*[@id="basic_email"]')
emailField.send_keys(email)
time.sleep(3)
passwordField = driver.find_element(by=By.XPATH, value='//*[@id="basic_password"]')
passwordField.send_keys(password)
time.sleep(3)

driver.quit()