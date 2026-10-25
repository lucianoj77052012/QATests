import pytest
import os
from pytest_bdd import given, when, then

@given("I navigated to hotel app link")
def login(browser, constants):
    browser.get(f"https://www.qacloud.dev/app-login.html?user={pytest.USERNAME}&app=hotel")
    browser.save_screenshot(os.path.join(pytest.SCREENSHOTS_PATH, "login.png"))
    print("Navigated successfully.")