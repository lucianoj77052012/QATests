import pytest
import os
from selenium.webdriver.common.by import By

SCREENSHOTS_PATH = os.path.join(".", "reports")

def take_full_page_screenshot(browser, request):
    required_width = browser.execute_script('return document.body.parentNode.scrollWidth')
    required_height = browser.execute_script('return document.body.parentNode.scrollHeight')
    browser.set_window_size(required_width, required_height)
    test_name = request.node.nodeid.split("::test_")[-1].split(".py")[0]
    browser.find_element(By.TAG_NAME, 'body').screenshot(os.path.join(SCREENSHOTS_PATH, f"{test_name}.png"))

def take_full_page_screenshot_playwright(page, request):
    test_name = request.node.nodeid.split("::test_")[-1].split(".py")[0]
    page.screenshot(path=os.path.join(SCREENSHOTS_PATH, f"playwright_{test_name}.png"))