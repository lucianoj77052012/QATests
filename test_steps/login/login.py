import pytest
import os
import time
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By

from test_steps.frontend.locators import Login
from test_steps.frontend.reports import take_full_page_screenshot

API_KEYS_FILENAME = "api_keys.txt"
USER_DATA_FILENAME = os.path.join("test_data", "user_data.csv")

class ApiKeysFileNotFoundException(Exception):
    pass

class ApiKeyNotFoundException(Exception):
    pass

class UserSession:

    def __init__(self, tester_purpose, user, api_key_name):
        self.tester_purpose = tester_purpose
        self.user = user
        self.api_key_name = api_key_name

@given(parsers.parse("I navigated to hotel app link as {tester_purpose}"), target_fixture="user_session")
def navigate_hotel_app_link(browser, tester_purpose):
    tester_purpose, user, api_key_name = get_user_data(tester_purpose)
    browser.get(f"https://www.qacloud.dev/app-login.html?user={user}&app=hotel")
    return UserSession(tester_purpose, user, api_key_name)

@when("I enter my credentials")
def enter_credentials(browser, user_session):
    username_input = browser.find_element(By.XPATH, Login.password)
    username_input.send_keys(get_api_key(user_session.user))
    login_button = browser.find_element(By.XPATH, Login.login_button)
    login_button.click()
    time.sleep(5)
    take_full_page_screenshot(browser)

def get_api_key(user):
    if not os.path.exists(API_KEYS_FILENAME):
        raise ApiKeysFileNotFoundException(f"File {API_KEYS_FILENAME} not found. This file is required for login. Please keep in mind the file is not included in the repository for security reasons -- you have to ask for it.")
    with open(API_KEYS_FILENAME) as api_keys_file:
        while True:
            api_key_next = api_keys_file.readline()
            if not api_key_next:
                raise ApiKeyNotFoundException(f"ApiKey for {user} not found in {API_KEYS_FILENAME}.")
            api_key_next_pair = api_key_next.split("=")
            user_in_file = api_key_next_pair[0]
            api_key_value = api_key_next_pair[1]
            if user_in_file == user:
                return api_key_value

def get_user_data(tester_purpose):
    with open(USER_DATA_FILENAME) as user_data_file:
        user_data_file.readline() #Intentionally skip the first line, which contains the separator to use.
        while True:
            tester_purpose_next = user_data_file.readline()
            if not tester_purpose_next:
                raise TesterPurposeNotFoundException(f"TesterPurpose {tester_purpose} not found in {USER_DATA_FILENAME}.")
            tester_purpose_next_row = tester_purpose_next.split(",")
            tester_purpose_in_file = tester_purpose_next_row[0]
            user_in_file = tester_purpose_next_row[1]
            api_key_name_in_file = tester_purpose_next_row[2]
            if tester_purpose_in_file == tester_purpose:
                return tester_purpose_in_file, user_in_file, api_key_name_in_file