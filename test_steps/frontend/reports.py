import pytest
import os

def take_screenshot(browser, constants):
    browser.save_screenshot(os.path.join(pytest.SCREENSHOTS_PATH, "login.png"))