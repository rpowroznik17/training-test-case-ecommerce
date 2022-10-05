"""
This module contains ShoppingCartPage,
page object for Luma - Magento eCommerce
shopping cart page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ShoppingCartPage:

    # Selectors

    CART_ITEM = (By.CSS_SELECTOR, "tbody[class='cart item']")
    UNIT_PRICE = (By.XPATH, "//td[@class='col price']//span[@class='price']")
    QUANTITY = (By.CSS_SELECTOR, "input[class='input-text qty']")
    SUBTOTAL_PRICE = (By.XPATH, "//td[@class='col subtotal']//span[@class='price']")
    TOTAL_PRICE = (By.XPATH, "//tr[@class='grand totals']//span")
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, "button.update")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def get_title(self):
        return self.browser.title

    def convert_to_float(self, price):
        price_sliced = price[1:]
        price_float = float(price_sliced)
        return price_float

    def get_all_products(self):
        all_products = self.browser.find_elements(*self.CART_ITEM)
        return all_products

    def get_unit_prices(self):
        unit_prices = self.browser.find_elements(*self.UNIT_PRICE)
        unit_prices_text = [price.text for price in unit_prices]
        unit_prices_converted = list(map(self.convert_to_float, unit_prices_text))
        return unit_prices_converted

    def get_quantities(self):
        quantities = self.browser.find_elements(*self.QUANTITY)
        quantities_text = [quantity.get_attribute("value") for quantity in quantities]
        quantities_converted = list(map(int, quantities_text))
        return quantities_converted

    def get_subtotal_prices(self):
        subtotal_prices = self.browser.find_elements(*self.SUBTOTAL_PRICE)
        subtotal_prices_text = [subtotal_price.text for subtotal_price in subtotal_prices]
        subtotal_prices_converted = list(map(self.convert_to_float, subtotal_prices_text))
        return subtotal_prices_converted

    def get_total_price(self):
        total_price = self.browser.find_element(*self.TOTAL_PRICE)
        total_price_text = total_price.text
        total_price_converted = self.convert_to_float(total_price_text)
        return total_price_converted

    def update_quantity(self, product_index, quantity):
        quantity_field = self.browser.find_elements(*self.QUANTITY)[product_index]
        quantity_field.send_keys(Keys.CONTROL, "a")
        quantity_field.send_keys(quantity)

    def click_update_cart_button(self):
        update_cart_button = self.browser.find_element(*self.UPDATE_CART_BUTTON)
        update_cart_button.click()
