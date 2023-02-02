import time

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By

class AddTaskPage(BasePageObject):

    xpath_start_date = "//input[@id='startDate']"
    xpath_task_name= "//input[@id='name']"
    xpath_picture = "//input[@id='picture']"
    xpath_task_title = "//div[contains(@class, 'ql-editor ql-blank')]"
    xpath_task_description = "(//div[contains(@class, 'ql-editor ql-blank')])[1]"
    xpath_save_button = "//button[@type='submit']"
    def __init__(self, driver):
        super().__init__(driver)

    def set_date(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_start_date).send_keys("2023-03-03")
            return self
    def set_name(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_task_name).send_keys("TaskPython")
            return self
    def set_title(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_task_title).send_keys("TaskPythonTaskPythonTaskPythonTaskPython")
            return self
    def set_description(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_task_description).send_keys("TaskPythonTaskPythonTaskPythonTaskPythonTaskPythonTaskPythonTaskPythonTaskPython")
            return self


    def save_task(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_save_button).click
            time.sleep(5)
            return self

    def set_path(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_picture).send_keys('')
            return self