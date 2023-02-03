import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://speak-ukrainian.org.ua/dev/")
btn = driver.find_element(by=By.XPATH, value='//*[@id="root"]/section/header/div[2]/ul/li[1]')
btn.click()
time.sleep(10)
div = driver.find_element(by=By.XPATH,
                          value='//*[@id="root"]/section/section/main/section/section/main/div/div[1]/div/div/div[1]/div[2]')
print(div.text)

driver.quit()
