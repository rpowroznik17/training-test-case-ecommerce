"""
This module contains SearchResultsPage,
page object for Luma - Magento eCommerce search results page
"""

from selenium.webdriver.common.by import By


class SearchResultsPage:

    # Selectors

    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.product-item-info")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def get_page_title(self):
        return self.browser.title

    def select_first_product(self):
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)
        search_results[0].click()

    def select_product_by_index(self, index):
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)
        search_results[index].click()

    def get_search_result_products(self):
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)
        return search_results


