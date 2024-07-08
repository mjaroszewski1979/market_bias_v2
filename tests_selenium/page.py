# Import WebDriverWait class with alias W
from selenium.webdriver.support.ui import WebDriverWait as W
# Import expected_conditions class with alias EC
from selenium.webdriver.support import expected_conditions as EC

# Import locators from the local module
from locators import ErrorPageLocators, HomePageLocators, AboutPageLocators, StrategiesPageLocators, ContactPageLocators



class BasePage(object):
    """
    Base page class containing common actions performed on web pages.
    """

    def __init__(self, driver):
        # Initialize with a web driver instance
        self.driver = driver

    def do_click(self, locator):
        # Wait for element to be visible and click it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_clear(self, locator):
        # Wait for element to be visible and clear its contents
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_send_keys(self, locator, text):
        # Wait for element to be visible and send text input to it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        # Wait for element to be visible and return it
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        # Wait for all elements to be visible and return them
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        # Wait for element to be visible and return its text
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def do_submit(self, locator):
        # Wait for element to be visible and submit it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()


class HomePage(BasePage):
    """
    Home page class containing specific actions performed on the home page.
    """
    
    def is_title_matches(self):
        # Check if the title matches the expected value
        return "Home - Market Bias" in self.driver.title

    def is_top_heading_displayed(self):
        # Get text of the top heading element
        heading_text = self.get_element_text(HomePageLocators.TOP_HEADING)
        # Return True if the expected text is found in the heading, else False
        return 'The Big Picture - Macro Perspective on the Capital Markets' in heading_text

    def is_about_link_works(self):
        # Click on the about link element
        self.do_click(HomePageLocators.ABOUT_LINK)
        # Return True if the title matches the expected value, else False
        return "About - Market Bias" in self.driver.title

    def is_logo_link_works(self):
        # Click on the logo link element
        self.do_click(HomePageLocators.LOGO)
        # Return True if the title matches the expected value, else False
        return "Home - Market Bias" in self.driver.title

    def is_strategies_link_works(self):
        # Click on the strategies link element
        self.do_click(HomePageLocators.STRATEGIES_LINK)
        # Return True if the title matches the expected value, else False
        return "Strategies - Market Bias" in self.driver.title

    def is_contact_link_works(self):
        # Click on the contact link element
        self.do_click(HomePageLocators.CONTACT_LINK)
        # Return True if the title matches the expected value, else False
        return "Contact - Market Bias" in self.driver.title

class AboutPage(BasePage):
    """
    About page class containing specific actions performed on the about page.
    """

    def is_title_matches(self):
        # Check if the title matches the expected value
        return "About - Market Bias" in self.driver.title

    def is_about_heading_displayed(self):
        # Get text of the about heading element
        about_heading = self.get_element_text(AboutPageLocators.ABOUT_HEADING)
        # Return True if the expected text is found in the heading, else False
        return 'Technical Analysis - The Forecasting of Future Financial Price Movements' in about_heading

class StrategiesPage(BasePage):
    """
    Strategies page class containing specific actions performed on the strategies page.
    """

    def is_title_matches(self):
        # Check if the title matches the expected value
        return "Strategies - Market Bias" in self.driver.title

    def is_strategies_heading_displayed(self):
        # Get text of the strategies heading element
        strategies_heading = self.get_element_text(StrategiesPageLocators.STRATEGIES_HEADING)
        # Return True if the expected text is found in the heading, else False
        return 'Momentum Investing - Buying Recent Stock Winners' in strategies_heading

 
class ContactPage(BasePage):
    """
    Contact page class containing specific actions performed on the contact page.
    """

    def is_title_matches(self):
        # Check if the title matches the expected value
        return "Contact - Market Bias" in self.driver.title

    def is_contact_heading_displayed(self):
        # Get text of the contact heading element
        contact_heading = self.get_element_text(ContactPageLocators.CONTACT_HEADING)
        # Return True if the expected text is found in the heading, else False
        return 'How to Achieve Success in Financial Markets' in contact_heading

    def is_contact_form_works(self):
        # Clear the name field element
        self.do_clear(ContactPageLocators.NAME)
        # Clear the email field element
        self.do_clear(ContactPageLocators.EMAIL)
        # Send keys to the name field element
        self.do_send_keys(ContactPageLocators.NAME, 'maciej')
        # Send keys to the email field element
        self.do_send_keys(ContactPageLocators.EMAIL, 'mj@gmail.com')
        # Submit the email field element
        self.do_submit(ContactPageLocators.EMAIL)
        # Return True if the title matches the expected value, else False
        return "Success - Market Bias" in self.driver.title 


class ErrorPage(BasePage):
    """
    Error page class containing specific actions performed on the error page.
    """

    def is_title_matches(self):
        # Check if the title matches the expected value
        return "Page Not Found - Market Bias" in self.driver.title

    def is_error_msg_displayed(self):
        # Get text of the error message element
        error_msg_text = self.get_element_text(ErrorPageLocators.ERROR_MSG)
        # Return True if the expected text is found in the error message, else False
        return "Sorry, we can’t find the website you were looking for." in error_msg_text




   
