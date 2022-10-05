"""
This module contains ProductPage,
page object for Luma - Magento eCommerce product page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductPage:

    # Selectors

    SIZE_OPTION = (By.CSS_SELECTOR, "div[option-label = 'L']")
    COLOR_OPTION = (By.CSS_SELECTOR, "div[option-label = 'Orange']")
    ADD_TO_WISHLIST_LINK = (By.CSS_SELECTOR, "a[data-action= 'add-to-wishlist']")
    ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")
    QUANTITY_FIELD = (By.NAME, "qty")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@data-ui-id= 'message-success']//div")
    CART_ICON = (By.CSS_SELECTOR, "a.showcart")
    VIEW_CART = (By.CSS_SELECTOR, "a.viewcart")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def choose_size(self):
        size_option = self.browser.find_element(*self.SIZE_OPTION)
        size_option.click()

    def choose_color(self):
        color_option = self.browser.find_element(*self.COLOR_OPTION)
        color_option.click()

    def add_to_wishlist(self):
        add_to_wishlist_link = self.browser.find_element(*self.ADD_TO_WISHLIST_LINK)
        add_to_wishlist_link.click()

    def fill_quantity_field(self, quantity):
        quantity_field = self.browser.find_element(*self.QUANTITY_FIELD)
        quantity_field.send_keys(Keys.CONTROL, "a")
        quantity_field.send_keys(quantity)

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_success_message(self):
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE)
        return success_message.text

    def navigate_to_cart(self):
        cart_icon = self.browser.find_element(*self.CART_ICON)
        cart_icon.click()

        view_cart = self.browser.find_element(*self.VIEW_CART)
        view_cart.click()
