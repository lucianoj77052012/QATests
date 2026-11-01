import time

from test_steps.frontend.AbstractFrontend import AbstractFrontend
from test_steps.frontend.playwright.PlaywrightReports import PlaywrightReports

class PlaywrightPage(AbstractFrontend):
    
    def __init__(self, page):
        self.page = page
        self.reports = PlaywrightReports(self.page)

    def navigate_to_url(self, url):
        self.page.goto(url)

    def type_in_element(self, element_xpath, text):
        self.page.fill(f"xpath={element_xpath}", text)

    def take_full_page_screenshot(self, request):
        self.reports.take_full_page_screenshot(request)

    def click_button(self, button_xpath):
        self.page.locator(f"xpath={button_xpath}").click()

    def verify_element_exists(self, element_xpath):
        retries = 5
        while retries:
            if self.page.query_selector(f"xpath={element_xpath}") is not None:
                return True
            time.sleep(1)
            retries -= 1
        return False

    def get_dropdown_selected_value(self, dropdown_xpath):
        return self.page.locator(f"xpath={dropdown_xpath}").evaluate("node => node.options[node.options.selectedIndex].textContent") #input_value() returns a dot.