import unittest

from selenium import webdriver

from page_object.home_page import HomePage
from settings.settings import base_web_url


class SearchTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(base_web_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_club_by_name(self):
        key_word = "American Gymnastics Club"
        name_club = HomePage(self.driver) \
            .enter_search_word(key_word)\
            .click_search_button()\
            .get_name_of_club()
        self.assertEqual(name_club, key_word)
