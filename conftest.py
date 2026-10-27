# Make sure conftest.py is in root. By loading it from root, directory changes such that the following lines are no longer required per test_execute file:

# Make the test_steps files accessible from current file.
# import os
# import sys
# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root_path)

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from test_steps.frontend.reports import take_full_page_screenshot

DRIVER_PATH = os.path.join(".", "chromedriver")

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    service = Service(DRIVER_PATH)
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(2)
    return browser

@pytest.fixture
def take_full_page_screenshot_wrapper(browser, request):
    yield #Wait until the test is done, then execute below code (take screenshot of final result, either success or fail).
    take_full_page_screenshot(browser, request)