"""
These tests cover adding product to
Luma - Magento eCommerce
"""

import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.account_details_page import AccountDetailsPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage


@pytest.mark.skip
def test_product_search(browser, registration_input):
    home_page = HomePage(browser)
    registration_page = RegistrationPage(browser)
    account_details_page = AccountDetailsPage(browser)
    search_result_page = SearchResultsPage(browser)

    input_for_registration = registration_input
    product_name = "t-shirt"
    page_title = "Search results"

    # Given the account details page is displayed
    home_page.load()
    home_page.navigate_to_register_page()

    registration_page.fill_all_required_fields(*input_for_registration)
    registration_page.submit_registration()

    # When the user searches for product
    account_details_page.search(product_name)

    # Then the page with search results is displayed
    title = search_result_page.get_page_title()
    assert page_title.lower() in title.lower()

    # And search results (products) are listed
    search_results = search_result_page.get_search_result_products()
    assert len(search_results) > 0


@pytest.mark.skip
def test_add_to_wishlist(browser, registration_input):

    # Pages
    home_page = HomePage(browser)
    registration_page = RegistrationPage(browser)
    account_details_page = AccountDetailsPage(browser)
    search_result_page = SearchResultsPage(browser)
    product_page = ProductPage(browser)
    wishlist_page = WishlistPage(browser)

    # Variables for testing purposes
    input_for_registration = registration_input
    product_name = "t-shirt"
    page_title = "My Wish List"
    message = "has been added to your Wish List"

    # Given the product page is displayed
    home_page.load()
    home_page.navigate_to_register_page()

    registration_page.fill_all_required_fields(*input_for_registration)
    registration_page.submit_registration()

    account_details_page.search(product_name)

    search_result_page.select_first_product()

    # And the size and color of the product are chosen
    product_page.choose_size()
    product_page.choose_color()

    # When the user clicks Add to wishlist link
    product_page.add_to_wishlist()

    # Then the wishlist page is displayed
    title = wishlist_page.get_title()
    assert page_title.lower() in title.lower()

    # And success message that product was added to the
    # wishlist is displayed
    success_message = wishlist_page.get_success_message()
    assert message.lower() in success_message.lower()

    # And the wishlist contains added product
    wishlist_products = wishlist_page.get_wishlist_products()
    assert len(wishlist_products) > 0


