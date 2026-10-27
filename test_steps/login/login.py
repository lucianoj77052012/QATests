import pytest
import os
import time
from pytest_bdd import given, when, then
from selenium.webdriver.common.by import By

from test_steps.frontend.locators import Login
from test_steps.frontend.reports import take_full_page_screenshot

API_KEYS_FILENAME = "api_keys.txt"

class ApiKeysFileNotFoundException(Exception):
    pass

class ApiKeyNotFoundException(Exception):
    pass

@given("I navigated to hotel app link")
def login(browser, constants):
    browser.get(f"https://www.qacloud.dev/app-login.html?user={pytest.USERNAME}&app=hotel")
    print("Navigated successfully.")

@when("I enter my credentials")
def enter_credentials(browser, constants):
    username_input = browser.find_element(By.XPATH, Login.password)
    username_input.send_keys(get_api_key("6PropertiesApiKey"))
    login_button = browser.find_element(By.XPATH, Login.login_button)
    login_button.click()
    time.sleep(5)
    take_full_page_screenshot(browser, constants)

def get_api_key(api_key_name):
    if not os.path.exists(API_KEYS_FILENAME):
        raise ApiKeysFileNotFoundException(f"File {API_KEYS_FILENAME} not found. This file is required for login. Please keep in mind the file is not included in the repository for security reasons -- you have to ask for it.")
    with open(API_KEYS_FILENAME) as api_keys_file:
        while True:
            api_key_next = api_keys_file.readline()
            if not api_key_next:
                raise ApiKeyNotFoundException(f"ApiKey for {api_key_name} not found in {API_KEYS_FILENAME}.")
            api_key_next_pair = api_key_next.split("=")
            api_key_name_in_file = api_key_next_pair[0]
            api_key_value = api_key_next_pair[1]
            if api_key_name_in_file == api_key_name:
                return api_key_value