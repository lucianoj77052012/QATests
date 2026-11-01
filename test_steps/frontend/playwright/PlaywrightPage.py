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