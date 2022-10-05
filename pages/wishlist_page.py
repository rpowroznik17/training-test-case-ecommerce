"""
This module contains WishlistPage,
page object for Luma - Magento eCommerce wishlist page
"""

from selenium.webdriver.common.by import By


class WishlistPage:

    # Selectors

    SUCCESS_MESSAGE = (By.XPATH, "//div[@data-ui-id= 'message-success']//div")
    WISHLIST_PRODUCTS = (By.XPATH, "//div[@class = 'products-grid wishlist']//div[@class = 'product-item-info']")
    ADD_ALL_TO_CART = (By.CSS_SELECTOR, "button[data-role='all-tocart']")
    LOGO = (By.CSS_SELECTOR, "a.logo")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def get_title(self):
        return self.browser.title

    def get_success_message(self):
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE)
        return success_message.text

    def get_wishlist_products(self):
        wishlist_products = self.browser.find_elements(*self.WISHLIST_PRODUCTS)
        return wishlist_products

    def add_all_to_cart(self):
        add_to_cart_button = self.browser.find_element(*self.ADD_ALL_TO_CART)
        add_to_cart_button.click()

    def return_to_main_menu(self):
        main_menu_link = self.browser.find_element(*self.LOGO)
        main_menu_link.click()
