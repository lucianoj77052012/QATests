# Make sure conftest.py is in root. By loading it from root, directory changes such that the following lines are no longer required per test_execute file:

# Make the test_steps files accessible from current file.
# import os
# import sys
# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root_path)

import os

import pytest

DRIVER_PATH = os.path.join(".", "chromedriver") #For Selenium solution.

class InvalidAutomationFrameworkException(Exception):
    pass

@pytest.fixture
def frontend():
    automation_framework = os.environ.get("env_automation_framework", None)
    if automation_framework is None:
        raise InvalidAutomationFrameworkException(f"Automation framework not set in environment variable.")
    if automation_framework == "selenium":
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from test_steps.frontend.selenium.SeleniumBrowser import SeleniumBrowser
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        service = Service(DRIVER_PATH)
        browser = webdriver.Chrome(service=service, options=options)
        browser.implicitly_wait(2)
        yield SeleniumBrowser(browser)
    elif automation_framework == "playwright":
        from playwright.sync_api import sync_playwright
        from test_steps.frontend.playwright.PlaywrightPage import PlaywrightPage
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            yield PlaywrightPage(page)
    else:
        raise InvalidAutomationFrameworkException(f"Provided automation framework {automation_framework} is not valid. Valid options: selenium, playwright.")

@pytest.fixture
def take_full_page_screenshot_wrapper(frontend, request):
    yield #Wait until the test is done, then execute below code (take screenshot of final result, either success or fail).
    frontend.take_full_page_screenshot(request)