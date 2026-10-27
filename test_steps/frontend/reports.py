import pytest
import os
from selenium.webdriver.common.by import By

def take_full_page_screenshot(browser, constants):
    required_width = browser.execute_script('return document.body.parentNode.scrollWidth')
    required_height = browser.execute_script('return document.body.parentNode.scrollHeight')
    browser.set_window_size(required_width, required_height)
    browser.find_element(By.TAG_NAME, 'body').screenshot(os.path.join(pytest.SCREENSHOTS_PATH, "login.png"))