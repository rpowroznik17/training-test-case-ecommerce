"""
This module contains HomePage,
page object for Luma - Magento eCommerce home page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    # URL

    URL = "https://magento.softwaretestingboard.com"

    # Selectors

    REGISTER_LINK = (By.XPATH, "//div[@class='panel header']//a[contains(@href, 'account/create')]")
    GEAR_NAV_LINK = (By.XPATH, "//a[contains(@href, 'gear.html')]")
    BAGS_NAV_LINK = (By.XPATH, "//a[contains(@href, 'bags.html')]")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def get_title(self):
        return self.browser.title

    def navigate_to_register_page(self):
        register_link = self.browser.find_element(*self.REGISTER_LINK)
        register_link.click()

    def navigate_to_bags(self):
        actions = ActionChains(self.browser)
        gear_nav_link = self.browser.find_element(*self.GEAR_NAV_LINK)
        bags_nav_link = self.browser.find_element(*self.BAGS_NAV_LINK)

        actions.move_to_element(gear_nav_link)
        actions.click(bags_nav_link)
        actions.perform()
