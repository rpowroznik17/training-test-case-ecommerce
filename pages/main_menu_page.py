"""
This module contains MainMenuPage,
page object for Luma - Magento eCommerce home page
"""

from selenium.webdriver.common.by import By


class HomePage:

    # URL

    URL = "https://magento.softwaretestingboard.com"

    # Selectors

    REGISTER_LINK = (By.XPATH, "//div[@class='panel header']//a[contains(@href, 'account/create')]")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def navigate_to_register_page(self):
        register_link = self.browser.find_element(*self.REGISTER_LINK)
        register_link.click()
