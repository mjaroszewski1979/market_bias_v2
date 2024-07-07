# Importing By class from selenium.webdriver.common.by for locating elements.
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """
    Class containing locators for elements on the Home page.
    """

    # Locator for the top heading element.
    TOP_HEADING = (By.CLASS_NAME, 'heading-top')
    
    # Locator for the About link element.
    ABOUT_LINK = (By.CLASS_NAME, 'about-link')

    # Locator for the logo element.
    LOGO = (By.CLASS_NAME, 'logo')

    # Locator for the Strategies link element.
    STRATEGIES_LINK = (By.CLASS_NAME, 'strategies-link')

    # Locator for the Contact link element.
    CONTACT_LINK = (By.CLASS_NAME, 'contact-link')

class AboutPageLocators(object):
    """
    Class containing locators for elements on the About page.
    """

    # Locator for the heading on the About page.
    ABOUT_HEADING = (By.CLASS_NAME, 'about-heading')

class StrategiesPageLocators(object):
    """
    Class containing locators for elements on the Strategies page.
    """

    # Locator for the heading on the Strategies page.
    STRATEGIES_HEADING = (By.CLASS_NAME, 'strategies-heading')

class ContactPageLocators(object):
    """
    Class containing locators for elements on the Contact page.
    """

    # Locator for the heading on the Contact page.
    CONTACT_HEADING = (By.CLASS_NAME, 'contact-heading')

    # Locator for the name input field.
    NAME = (By.NAME, 'name')

    # Locator for the email input field.
    EMAIL = (By.NAME, 'email')

    # Locator for the submit button on the Contact page.
    SUBMIT = (By.CLASS_NAME, 'button')

class ErrorPageLocators(object):
    """
    Class containing locators for elements on the Error page.
    """

    # Locator for the error message element on the Error page.
    ERROR_MSG = (By.CLASS_NAME, 'error-msg')

