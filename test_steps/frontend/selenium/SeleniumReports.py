import os

from selenium.webdriver.common.by import By

SCREENSHOTS_PATH = os.path.join(".", "reports", "selenium")

class SeleniumReports:

    def __init__(self, browser):
        self.browser = browser

    def take_full_page_screenshot(self, request):
        required_width = self.browser.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.browser.execute_script('return document.body.parentNode.scrollHeight')
        self.browser.set_window_size(required_width, required_height)
        test_name = request.node.nodeid.split("::test_")[-1].split(".py")[0]
        self.browser.find_element(By.TAG_NAME, 'body').screenshot(os.path.join(SCREENSHOTS_PATH, f"{test_name}.png"))