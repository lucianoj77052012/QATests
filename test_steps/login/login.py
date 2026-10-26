import pytest
import os
from pytest_bdd import given, when, then
from selenium.webdriver.common.by import By

from test_steps.frontend.locators import Login
from test_steps.frontend.reports import take_screenshot

@given("I navigated to hotel app link")
def login(browser, constants):
    browser.get(f"https://www.qacloud.dev/app-login.html?user={pytest.USERNAME}&app=hotel")
    print("Navigated successfully.")

@when("I enter my credentials")
def enter_credentials(browser, constants):
    username_input = browser.find_element(By.XPATH, Login.password)
    username_input.send_keys("updated")
    take_screenshot(browser, constants)