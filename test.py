import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://speak-ukrainian.org.ua/dev/")
search =driver.find_element(by=By.XPATH, value='//*[@id="rc_select_0"]')
search.send_keys("Jerome IT School")
time.sleep(10)
club = driver.find_element(by=By.XPATH, value='//*[@id="root"]/section/section/main/section/section/main/div/div/div/div/div[1]/div[2]')
club.click()
time.sleep(3)
driver.get("https://speak-ukrainian.org.ua/dev/")
addClub = driver.find_element(by=By.XPATH, value='//*[@id="root"]/section/header/div[3]/button')
addClub.click()
time.sleep(3)
email = driver.find_element(by=By.XPATH, value='//*[@id="basic_email"]')
email.send_keys("admin@gmail.com")
time.sleep(3)
password = driver.find_element(by=By.XPATH, value='//*[@id="basic_password"]')
password.send_keys("1234567")
time.sleep(3)
submit = driver.find_element(by=By.XPATH, value='//*[@id="basic"]/div[2]/div[3]/div/div/div/div/div/button')
submit.click()
time.sleep(3)

driver.quit()