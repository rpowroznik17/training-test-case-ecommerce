import random
import json
import pytest
import selenium.webdriver


@pytest.fixture(scope="session")
def config():

    # Read the config file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config["browser"] in ["Chrome", "Firefox", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # Return config file
    return config


@pytest.fixture(scope="session")
def test_data():

    # Read the test data file
    with open("test_data.json") as test_data_file:
        test_data = json.load(test_data_file)

    # Return test data file
    return test_data


@pytest.fixture
def browser(config):

    # Initialize webdriver instance

    match config["browser"]:
        case "Chrome":
            b = selenium.webdriver.Chrome()
        case "Firefox":
            b = selenium.webdriver.Firefox()
        case "Headless Chrome":
            opts = selenium.webdriver.ChromeOptions()
            opts.add_argument("headless")
            b = selenium.webdriver.Chrome(options=opts)
        case _:
            raise Exception(f'Browser {config["browser"]} is not supported')

    # Make its calls wait up 10 seconds for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # Return webdriver instance for the setup
    yield b

    # Quit the webdriver instance for the cleanup
    b.quit()


@pytest.fixture
def registration_input(test_data):
    random_number = random.randint(1, 9999)

    firstname = test_data["firstname"]
    lastname = test_data["lastname"]
    email_address = f"{firstname}.{lastname}{random_number}@example.com"
    password = test_data["password"]
    return (firstname, lastname, email_address, password)
