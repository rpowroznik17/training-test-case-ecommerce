"""
These tests cover registration to
Luma - Magento eCommerce and then adding item
to wishlist and shopping cart
"""

import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.account_details_page import AccountDetailsPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage
from pages.shopping_cart_page import ShoppingCartPage


def test_complete_case(browser, registration_input, test_data):

    # Pages
    home_page = HomePage(browser)
    registration_page = RegistrationPage(browser)
    account_details_page = AccountDetailsPage(browser)
    search_result_page = SearchResultsPage(browser)
    product_page = ProductPage(browser)
    wishlist_page = WishlistPage(browser)
    shopping_cart_page = ShoppingCartPage(browser)

    # Load homepage and navigate to registration page
    home_page.load()
    home_page.navigate_to_register_page()

    # Fill some input fields in registration form and click
    # 'Create an Account' button
    registration_page.fill_some_fields(test_data['firstname'], test_data['lastname'])
    registration_page.submit_registration()

    # Check if proper notifications show up
    field_required_notifications = registration_page.get_field_required_notifications()
    for notification in field_required_notifications:
        print(f"Notification: '{notification}' equals desired '{test_data['field_required_notification']}'")
        assert notification == test_data['field_required_notification']

    # Fill all required input fields in registration form
    # and click 'Create an Account' button
    registration_page.fill_all_required_fields(*registration_input)
    registration_page.submit_registration()

    # Check if message that account has been created is displayed
    account_created_message = account_details_page.get_success_message()
    print(f"Check if '{test_data['success_message_registration']}' in '{account_created_message}'")
    assert test_data['success_message_registration'] in account_created_message

    # Search for product
    account_details_page.search(test_data['searched_product'])

    # Check if products are listed
    search_results = search_result_page.get_search_result_products()
    print(f"Number of search results: {len(search_results)}")
    assert len(search_results) > 0

    # Choose first product from list
    search_result_page.select_first_product()

    # Choose color and size of product
    product_page.choose_color()
    product_page.choose_size()

    # Add product to wishlist
    product_page.add_to_wishlist()

    # Wishlist page is displayed

    # Success message that product was added to the
    # wishlist is displayed
    added_to_wishlist_message = wishlist_page.get_success_message()
    print(f"Check if '{test_data['success_message_wishlist']}' in '{added_to_wishlist_message}'")
    assert test_data['success_message_wishlist'] in added_to_wishlist_message

    # Wishlist contains added product
    wishlist_products = wishlist_page.get_wishlist_products()
    print(f"Number of wishlist products: {len(wishlist_products)}")
    assert len(wishlist_products) > 0

    # Add products from wishlist to cart
    wishlist_page.add_all_to_cart()

    # Success message that product(s) was added to the
    # cart is displayed
    added_to_cart_message = wishlist_page.get_success_message()
    print(f"Check if '{test_data['success_message_wishlist_add_to_cart']}' in '{added_to_cart_message}'")
    assert test_data['success_message_wishlist_add_to_cart'] in added_to_cart_message

    # Return to main menu page
    wishlist_page.return_to_main_menu()

    # Navigate to bags
    home_page.navigate_to_bags()

    # Page with bags is displayed
    assert test_data['title_bags'] in home_page.get_title()

    # All bags are listed
    search_results = search_result_page.get_search_result_products()
    print(f"Number of bags: {len(search_results)}")
    assert len(search_results) > 0

    # Choose a bag and click it
    search_result_page.select_product_by_index(2)

    # In quantity field provide number of bags
    product_page.fill_quantity_field(test_data['quantity_first'])

    # Click "Add to Cart" button
    product_page.add_to_cart()

    # Success message that you added a product
    # to shopping cart
    added_to_cart_message = product_page.get_success_message()
    print(f"Check if '{test_data['success_message_product_page_add_to_cart']}' in '{added_to_cart_message}'")
    assert test_data['success_message_product_page_add_to_cart'] in added_to_cart_message

    # Navigate to shopping cart
    product_page.navigate_to_cart()

    # All added products are listed
    shopping_cart_products = shopping_cart_page.get_all_products()
    print(f"Number of products in shopping cart: {len(shopping_cart_products)}")
    assert len(shopping_cart_products) > 0

    # Quantity of bags is correct
    quantity_of_bags = shopping_cart_page.get_quantities()[1]
    print(f"Quantity of bags: {quantity_of_bags}")
    assert quantity_of_bags == test_data['quantity_first']

    # Total price is calculated correctly
    total_price_summary = shopping_cart_page.get_total_price()
    print(f"Total price in summary: {total_price_summary}")
    total_price_actual = 0.0

    unit_prices = shopping_cart_page.get_unit_prices()
    quantities = shopping_cart_page.get_quantities()

    for i in range(len(unit_prices)):
        total_price_actual += quantities[i] * unit_prices[i]
        print(f"Actual total price sum: {total_price_actual}")

    print(f"Actual total price after sum: {total_price_actual}")
    assert total_price_actual == total_price_summary

    # Change quantity of bags and click 'Update Shopping Cart' button
    shopping_cart_page.update_quantity(1, test_data['quantity_second'])
    shopping_cart_page.click_update_cart_button()

    # Quantity of bags is changed
    updated_quantity_of_bags = shopping_cart_page.get_quantities()[1]
    print(f"\nUpdated quantity of bags: {updated_quantity_of_bags}")
    assert updated_quantity_of_bags == test_data['quantity_second']

    # Total price for bags is updated properly
    subtotal_price_bags = shopping_cart_page.get_subtotal_prices()[1]
    print(f"Subtotal price for bags: {subtotal_price_bags}")

    unit_prices_bags = shopping_cart_page.get_unit_prices()[1]
    price_bags_actual = unit_prices_bags * updated_quantity_of_bags
    print(f"Subtotal actual price for bags: {price_bags_actual}")
    assert price_bags_actual == subtotal_price_bags

    # Total price for all products is updated properly
    total_price_summary = shopping_cart_page.get_total_price()
    print(f"Total price in summary: {total_price_summary}")
    total_price_actual = 0.0

    unit_prices = shopping_cart_page.get_unit_prices()
    quantities = shopping_cart_page.get_quantities()

    for i in range(len(unit_prices)):
        total_price_actual += quantities[i] * unit_prices[i]
        print(f"Total price actual sum: {total_price_actual}")

    print(f"Total price actual after sum: {total_price_actual}")
    assert total_price_actual == total_price_summary
