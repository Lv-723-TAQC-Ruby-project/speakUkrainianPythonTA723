import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from jproperties import Properties

xpath_profile_menu_button = "//div[contains(@class, 'user-profile')]"
xpath_enter_button = "//div[contains(text(), 'Увійти')]"
xpath_email_input = "//input[@id='basic_email']"
xpath_password_input = "//input[@id='basic_password']"
xpath_login_button = "//button[contains(@class, 'login-button')]"
text_to_check = "Додати центр"

configs = Properties()
with open('config.properties', 'rb') as config_file:
    configs.load(config_file)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(configs.get("base_web_url").data)
driver.find_element(by=By.XPATH, value=xpath_profile_menu_button).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=xpath_enter_button).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=xpath_email_input).send_keys(configs.get("admin_email").data)
driver.find_element(by=By.XPATH, value=xpath_password_input).send_keys(configs.get("admin_password").data)
driver.find_element(by=By.XPATH, value=xpath_login_button).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=xpath_profile_menu_button).click()
if text_to_check in driver.page_source:
    print("Тест успішно пройдено")
else:
    print("Тест провалено")
