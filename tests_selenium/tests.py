# Import the sys module for system-specific parameters and functions
import sys
# Import the os module for interacting with the operating system
import os
# Import the unittest module for creating test cases
import unittest
# Import the selenium web driver
from selenium import webdriver

# Get the directory name of the current file
current = os.path.dirname(os.path.realpath(__file__)) 
# Get the parent directory name of the current directory
parent = os.path.dirname(current)
# Add the parent directory to the system path to enable module imports
sys.path.append(parent)


# Import the page module for page object classes
import page
# Import the create_app function from the run module
from run import create_app


class TestBase(unittest.TestCase):
    """
    Base test class containing setup and teardown methods.
    """

    def setUp(self):
        # Create an instance of the application and push the app context
        app = create_app()
        app.app_context().push()
        # Initialize the Chrome web driver
        self.driver =  webdriver.Chrome('chromedriver.exe')
        # Set the window size of the browser
        self.driver.set_window_size(1920, 1080)

    def tearDown(self):
        # Close the web driver after each test
        self.driver.close()


class SeleniumTest(TestBase):
    """
    Selenium test class containing specific tests for web pages.
    """
        
    def test_home_page(self):
        # Navigate to the home page
        self.driver.get('http://127.0.0.1:5000/')
        # Create an instance of the HomePage class
        home_page = page.HomePage(self.driver)
        # Assert that the title matches the expected value
        assert home_page.is_title_matches()
        # Assert that the top heading is displayed correctly
        assert home_page.is_top_heading_displayed()
        # Assert that the about link works correctly
        assert home_page.is_about_link_works()
        # Assert that the logo link works correctly
        assert home_page.is_logo_link_works()
        # Assert that the strategies link works correctly
        assert home_page.is_strategies_link_works()
        # Assert that the contact link works correctly
        assert home_page.is_contact_link_works()

    def test_about_page(self):
        # Navigate to the about page
        self.driver.get('http://127.0.0.1:5000/about')
        # Create an instance of the AboutPage class
        about_page = page.AboutPage(self.driver)
        # Assert that the title matches the expected value
        assert about_page.is_title_matches()
        # Assert that the about heading is displayed correctly
        assert about_page.is_about_heading_displayed()

    def test_strategies_page(self):
        # Navigate to the strategies page
        self.driver.get('http://127.0.0.1:5000/strategies')
        # Create an instance of the StrategiesPage class
        strategies_page = page.StrategiesPage(self.driver)
        # Assert that the title matches the expected value
        assert strategies_page.is_title_matches()
        # Assert that the strategies heading is displayed correctly
        assert strategies_page.is_strategies_heading_displayed()

    def test_contact_page(self):
        # Navigate to the contact page
        self.driver.get('http://127.0.0.1:5000/contact')
        # Create an instance of the ContactPage class
        contact_page = page.ContactPage(self.driver)
        # Assert that the title matches the expected value
        assert contact_page.is_title_matches()
        # Assert that the contact heading is displayed correctly
        assert contact_page.is_contact_heading_displayed()
        # Assert that the contact form works correctly
        assert contact_page.is_contact_form_works()

    def test_error_page(self):
        # Navigate to a non-existing page to trigger the error page
        self.driver.get('http://127.0.0.1:5000/not_found')
        # Create an instance of the ErrorPage class
        error_page = page.ErrorPage(self.driver)
        # Assert that the title matches the expected value
        assert error_page.is_title_matches()
        # Assert that the error message is displayed correctly
        assert error_page.is_error_msg_displayed()
        


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()


        
