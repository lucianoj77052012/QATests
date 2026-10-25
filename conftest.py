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

USERNAME = "Luciano"
DRIVER_PATH = os.path.join(".", "chromedriver")
SCREENSHOTS_PATH = os.path.join(".", "reports")

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    service = Service(DRIVER_PATH)
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(f"https://www.qacloud.dev/app-login.html?user={USERNAME}&app=hotel")
    browser.save_screenshot(os.path.join(SCREENSHOTS_PATH, "login.png"))