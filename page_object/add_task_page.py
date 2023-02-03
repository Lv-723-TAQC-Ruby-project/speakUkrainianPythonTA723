import time

from selenium.webdriver import ActionChains

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By

class AddTaskPage(BasePageObject):

    xpath_start_date = "//input[@id='startDate']"
    xpath_task_name = "//input[@id='name']"
    xpath_picture = "//input[@id='picture']"
    xpath_task_title = "//div[contains(@class, 'ql-editor ql-blank')]"
    xpath_task_description = "(//div[contains(@class, 'ql-editor ql-blank')])[1]"
    xpath_save_button = "/html/body/div[1]/section/section/main/div/form/div[7]/div/div/div/div/button"
    xpath_error_message = "//div[@class='ant-message']"
    def __init__(self, driver):
        super().__init__(driver)

    def set_date(self,date):
            self.driver.find_element(by=By.XPATH, value=self.xpath_start_date).send_keys(date)
            return self
    def set_path(self,path):
        self.driver.find_element(by=By.XPATH, value=self.xpath_picture).send_keys(path)
        return self
    def set_name(self,name):
            self.driver.find_element(by=By.XPATH, value=self.xpath_task_name).send_keys(name)
            return self
    def set_title(self,title):
            self.driver.find_element(by=By.XPATH, value=self.xpath_task_title).send_keys(title)
            return self
    def set_description(self,description):
            self.driver.find_element(by=By.XPATH, value=self.xpath_task_description).send_keys(description)
            return self

    def save_task(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_save_button).click()
            time.sleep(5)
            return self
    def get_error_message(self):
        print(self.driver.find_element(by=By.XPATH, value=self.xpath_error_message))
        return self
    def message(self):
        self.driver.find_element(by=By.XPATH, value="//div[@class='ant-message']").text()
        return self

