import unittest

from settings.settings import base_web_url

from selenium import webdriver

from page_object.home_page import HomePage


class RegisterTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(base_web_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register(self):
        HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_register_button() \
            .enter_register_data() \
            .click_exit_button() \
            .click_drop_down_menu() \
            .click_register_button()
        self.assertIn("Test", self.driver.page_source)
        self.assertIn("Daisy", self.driver.page_source)
        self.assertIn("daisy@gmail.com", self.driver.page_source)
        self.assertIn("0673456785", self.driver.page_source)
        self.assertIn("123456789", self.driver.page_source)
        self.assertIn("123456789", self.driver.page_source)
