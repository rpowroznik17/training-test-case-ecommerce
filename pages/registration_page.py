"""
This module contains RegistrationPage,
page object for Luma - Magento eCommerce registration page
"""

from selenium.webdriver.common.by import By


class RegistrationPage:

    # Selectors

    FIRSTNAME = (By.ID, "firstname")
    LASTNAME = (By.ID, "lastname")
    EMAIL_ADDRESS = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRMATION = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.submit")
    FIELD_REQUIRED_NOTIFICATION = (By.CSS_SELECTOR, "div.mage-error")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def fill_some_fields(self, firstname, lastname):
        firstname_field = self.browser.find_element(*self.FIRSTNAME)
        firstname_field.send_keys(firstname)

        lastname_field = self.browser.find_element(*self.LASTNAME)
        lastname_field.send_keys(lastname)

    def fill_all_required_fields(self, firstname, lastname, email_address, password):
        firstname_field = self.browser.find_element(*self.FIRSTNAME)
        firstname_field.send_keys(firstname)

        lastname_field = self.browser.find_element(*self.LASTNAME)
        lastname_field.send_keys(lastname)

        email_address_field = self.browser.find_element(*self.EMAIL_ADDRESS)
        email_address_field.send_keys(email_address)

        password_field = self.browser.find_element(*self.PASSWORD)
        password_field.send_keys(password)

        password_confirmation_field = self.browser.find_element(*self.PASSWORD_CONFIRMATION)
        password_confirmation_field.send_keys(password)

    def submit_registration(self):
        submit_button = self.browser.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()

    def get_field_required_notifications(self):
        field_required_notifications = self.browser.find_elements(*self.FIELD_REQUIRED_NOTIFICATION)
        notifications = [n.text for n in field_required_notifications]
        return notifications

