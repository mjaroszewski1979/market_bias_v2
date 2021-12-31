from selenium.webdriver.common.by import By

class HomePageLocators(object):

    TOP_HEADING = (By.CLASS_NAME, 'heading-top')
    ABOUT_LINK = (By.CLASS_NAME, 'about-link')
    LOGO = (By.CLASS_NAME, 'logo')
    STRATEGIES_LINK = (By.CLASS_NAME, 'strategies-link')
    CONTACT_LINK = (By.CLASS_NAME, 'contact-link')

class AboutPageLocators(object):

    ABOUT_HEADING = (By.CLASS_NAME, 'about-heading')

class StrategiesPageLocators(object):

    STRATEGIES_HEADING = (By.CLASS_NAME, 'strategies-heading')

class ContactPageLocators(object):

    CONTACT_HEADING = (By.CLASS_NAME, 'contact-heading')
    NAME = (By.NAME, 'name')
    EMAIL = (By.NAME, 'email')
    SUBMIT = (By.CLASS_NAME, 'button')

class ErrorPageLocators(object):

    ERROR_MSG = (By.CLASS_NAME, 'error-msg')

