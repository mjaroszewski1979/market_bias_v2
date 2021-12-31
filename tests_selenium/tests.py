import sys
import os

current = os.path.dirname(os.path.realpath(__file__)) 
parent = os.path.dirname(current)
sys.path.append(parent)

from selenium import webdriver
import page
from run import create_app
import unittest





class TestBase(unittest.TestCase):


    def setUp(self):
        app = create_app()
        app.app_context().push()
        self.driver =  webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_size(1920, 1080)


    def tearDown(self):
        self.driver.close()


class SeleniumTest(TestBase):
        
    def test_home_page(self):
        self.driver.get('http://127.0.0.1:5000/')
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_top_heading_displayed()
        assert home_page.is_about_link_works()
        assert home_page.is_logo_link_works()
        assert home_page.is_strategies_link_works()
        assert home_page.is_contact_link_works()

    def test_about_page(self):
        self.driver.get('http://127.0.0.1:5000/about')
        about_page = page.AboutPage(self.driver)
        assert about_page.is_title_matches()
        assert about_page.is_about_heading_displayed()

    def test_strategies_page(self):
        self.driver.get('http://127.0.0.1:5000/strategies')
        strategies_page = page.StrategiesPage(self.driver)
        assert strategies_page.is_title_matches()
        assert strategies_page.is_strategies_heading_displayed()

    def test_contact_page(self):
        self.driver.get('http://127.0.0.1:5000/contact')
        contact_page = page.ContactPage(self.driver)
        assert contact_page.is_title_matches()
        assert contact_page.is_contact_heading_displayed()
        assert contact_page.is_contact_form_works()

    def test_error_page(self):
        self.driver.get('http://127.0.0.1:5000/not_found')
        error_page = page.ErrorPage(self.driver)
        assert error_page.is_title_matches()
        assert error_page.is_error_msg_displayed()
        


if __name__ == '__main__':
    unittest.main()


        