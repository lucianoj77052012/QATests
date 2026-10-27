import pytest
import os
import time
from pytest_bdd import given, when, then
from selenium.webdriver.common.by import By

from test_steps.frontend.locators import Login
from test_steps.frontend.reports import take_full_page_screenshot

@given("I navigated to hotel app link")
def login(browser, constants):
    browser.get(f"https://www.qacloud.dev/app-login.html?user={pytest.USERNAME}&app=hotel")
    print("Navigated successfully.")

@when("I enter my credentials")
def enter_credentials(browser, constants):
    username_input = browser.find_element(By.XPATH, Login.password)
    username_input.send_keys(get_api_key())
    login_button = browser.find_element(By.XPATH, Login.login_button)
    login_button.click()
    time.sleep(5)
    take_full_page_screenshot(browser, constants)

def get_api_key():
    with open("api_keys.txt") as api_keys_file:
        return api_keys_file.readline()