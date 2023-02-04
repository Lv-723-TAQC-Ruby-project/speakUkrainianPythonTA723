import unittest

from selenium import webdriver

from page_object.home_page import HomePage
from settings.settings import admin_email, admin_password
from settings.settings import base_web_url


class OpenTaskPageTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(base_web_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_task_without_challenge(self):
        HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials(admin_email,admin_password)\
            .click_drop_down_menu() \
            .add_task()\
            .click_add_task()\
            .set_date("2023-03-03") \
            .set_path("C:\\Users\\lovel\\OneDrive\\Desktop\\R.jpeg") \
            .set_name("TaskPython") \
            .set_title("TaskPythonTaskPythonTaskPythonTaskPython") \
            .set_description("TaskPythonTaskPythonTaskPythonTaskPythonTaskPythonTaskPythonTaskPythonTaskPython") \
            .save_task()
        self.assertTrue("Please,select challenge")