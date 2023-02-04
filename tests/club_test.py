import unittest
from selenium import webdriver
from page_object.home_page import HomePage
from page_object.home_page import AddClubModel
from settings.settings import (base_web_url,
                               admin_email,
                               admin_password)


class ClubTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(base_web_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_invalid_name_creating_club(self):
        name_club = "test"
        name_club2 = "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttestt"
        name_club3 = "ЫЭЪЫЭЪ"
        HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials(admin_email, admin_password) \
            .click_drop_down_menu()\
            .click_add_club_button()\
            .enter_name_club(name_club)
        self.assertIn("Некоректна назва гуртка", self.driver.page_source)

        AddClubModel(self.driver)\
            .enter_name_club(name_club2)
        self.assertIn("Некоректна назва гуртка", self.driver.page_source)

        AddClubModel(self.driver) \
            .enter_name_club(name_club3)
        self.assertIn("Некоректна назва гуртка", self.driver.page_source)



