"""
This module contains AccountDetailsPage,
page object for Luma - Magento eCommerce account details page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AccountDetailsPage:

    # Selectors

    SUCCESS_MESSAGE = (By.XPATH, "//div[@data-ui-id='message-success']/div")
    SEARCH_INPUT = (By.ID, "search")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def get_page_title(self):
        return self.browser.title

    def get_success_message(self):
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE)
        return success_message.text

    def search(self, searched_item):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(searched_item + Keys.RETURN)

