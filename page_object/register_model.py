import time



from page_object.base_page_object import BasePageObject

from selenium.webdriver.common.by import By



class RegisterModel(BasePageObject):
    xpath_name_input = "//input[@id='firstName']"
    xpath_last_name_input = "//input[@id='lastName']"
    xpath_user_pass_input = "//input[@id='password']"
    xpath_confirm_pass_input = "//input[@id='confirm']"
    xpath_exit_button = "//button[contains(@class, 'ant-modal-close')]"
    xpath_phone_input = "//input[@id='phone']"
    xpath_user_email_input = "//input[@id='email']"
    xpath_content = "//span[contains(text(), 'Контент')]"
    xpath_challenges = "//span[contains(text(), 'Челенджі')]"
    xpath_task = "//a[contains(text(), 'Завдання')]"


    def __init__(self, driver):
        super().__init__(driver)

    def enter_name(self,name):
            self.driver.find_element(by=By.XPATH, value=self.xpath_name_input).send_keys(name)
            return self
    def enter_last_name(self,last_name):
            self.driver.find_element(by=By.XPATH, value=self.xpath_last_name_input).send_keys(last_name)
            return self
    def enter_email(self,email):
            self.driver.find_element(by=By.XPATH, value=self.xpath_user_email_input).send_keys(email)
            return self

    def enter_phone(self,phone):
            self.driver.find_element(by=By.XPATH, value=self.xpath_phone_input).send_keys(phone)
            return self

    def enter_password(self,password):
            self.driver.find_element(by=By.XPATH, value=self.xpath_user_pass_input).send_keys(password)
            return self

    def enter_confirm_pass(self,confirm):
            self.driver.find_element(by=By.XPATH, value=self.xpath_confirm_pass_input).send_keys(confirm)
            return self

    def click_exit_button(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_exit_button).click()
            time.sleep(3)
            from page_object.home_page import HomePage
            return HomePage(self.driver)