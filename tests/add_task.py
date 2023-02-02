import unittest

from page_object.add_task_page import AddTaskPage

from page_object.task_page import TaskPage

from settings.settings import base_web_url

from selenium import webdriver

from page_object.home_page import HomePage


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

    def test_task(self):
        HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials() \
            .click_drop_down_menu() \
            .add_task()
        TaskPage(self.driver) \
            .click_add_task()
        AddTaskPage(self.driver) \
            .set_date() \
            .set_name() \
            .set_title() \
            .set_description() \
            .save_task()

        self.assertIn("Завдання", self.driver.page_source)