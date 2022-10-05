"""
These tests cover registration to
Luma - Magento eCommerce
"""

import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.account_details_page import AccountDetailsPage


@pytest.mark.skip
def test_register_invalid(browser):
    home_page = HomePage(browser)
    registration_page = RegistrationPage(browser)

    registration_input_invalid = ("John", "Smith")
    field_required_notification = "This is a required field."

    # Given the registration page is displayed
    home_page.load()
    home_page.navigate_to_register_page()

    # When the user fills some required fields and clicks "Create an account"
    registration_page.fill_some_fields(*registration_input_invalid)
    registration_page.submit_registration()

    # Then there are error messages next to not filled fields
    field_required_notifications = registration_page.get_field_required_notifications()
    for notification in field_required_notifications:
        print(f"Notification: {notification} equals desired {field_required_notification}")
        assert notification == field_required_notification


@pytest.mark.skip
def test_register_valid(browser, registration_input):
    home_page = HomePage(browser)
    registration_page = RegistrationPage(browser)
    account_details_page = AccountDetailsPage(browser)

    input_for_registration = registration_input
    page_title = "My Account"
    success_message = "Thank you for registering"

    # Given the registration page is displayed
    home_page.load()
    home_page.navigate_to_register_page()

    # When the user fills all required fields and clicks "Create an account"
    registration_page.fill_all_required_fields(*input_for_registration)
    registration_page.submit_registration()

    # Then page with account details is displayed
    title = account_details_page.get_page_title()
    assert page_title.lower() in title.lower()

    # And message that account has been created is displayed
    message = account_details_page.get_success_message()
    assert success_message.lower() in message.lower()

