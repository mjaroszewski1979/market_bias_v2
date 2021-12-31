from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from locators import ErrorPageLocators, HomePageLocators, AboutPageLocators, StrategiesPageLocators, ContactPageLocators



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()


class HomePage(BasePage):

    def is_title_matches(self):
        return "Home - Market Bias" in self.driver.title

    def is_top_heading_displayed(self):
        heading_text = self.get_element_text(HomePageLocators.TOP_HEADING)
        return 'The Big Picture - Macro Perspective on the Capital Markets' in heading_text

    def is_about_link_works(self):
        self.do_click(HomePageLocators.ABOUT_LINK)
        return "About - Market Bias" in self.driver.title

    def is_logo_link_works(self):
        self.do_click(HomePageLocators.LOGO)
        return "Home - Market Bias" in self.driver.title

    def is_strategies_link_works(self):
        self.do_click(HomePageLocators.STRATEGIES_LINK)
        return "Strategies - Market Bias" in self.driver.title

    def is_contact_link_works(self):
        self.do_click(HomePageLocators.CONTACT_LINK)
        return "Contact - Market Bias" in self.driver.title

class AboutPage(BasePage):

    def is_title_matches(self):
        return "About - Market Bias" in self.driver.title

    def is_about_heading_displayed(self):
        about_heading = self.get_element_text(AboutPageLocators.ABOUT_HEADING)
        return 'Technical Analysis - The Forecasting of Future Financial Price Movements' in about_heading

class StrategiesPage(BasePage):

    def is_title_matches(self):
        return "Strategies - Market Bias" in self.driver.title

    def is_strategies_heading_displayed(self):
        strategies_heading = self.get_element_text(StrategiesPageLocators.STRATEGIES_HEADING)
        return 'Momentum Investing - Buying Recent Stock Winners' in strategies_heading

 
class ContactPage(BasePage):

    def is_title_matches(self):
        return "Contact - Market Bias" in self.driver.title

    def is_contact_heading_displayed(self):
        contact_heading = self.get_element_text(ContactPageLocators.CONTACT_HEADING)
        return 'How to Achieve Success in Financial Markets' in contact_heading

    def is_contact_form_works(self):
        self.do_clear(ContactPageLocators.NAME)
        self.do_clear(ContactPageLocators.EMAIL)
        self.do_send_keys(ContactPageLocators.NAME, 'maciej')
        self.do_send_keys(ContactPageLocators.EMAIL, 'mj@gmail.com')
        self.do_submit(ContactPageLocators.EMAIL)
        return "Success - Market Bias" in self.driver.title 


class ErrorPage(BasePage):

    def is_title_matches(self):
        return "Page Not Found - Market Bias" in self.driver.title

    def is_error_msg_displayed(self):
        error_msg_text = self.get_element_text(ErrorPageLocators.ERROR_MSG)
        return "Sorry, we can’t find the website you were looking for." in error_msg_text




   