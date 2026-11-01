from test_steps.frontend.AbstractFrontend import AbstractFrontend
from test_steps.frontend.selenium.SeleniumReports import SeleniumReports
from selenium.webdriver.common.by import By

class SeleniumBrowser(AbstractFrontend):
    
    def __init__(self, browser):
        self.browser = browser
        self.reports = SeleniumReports(self.browser)

    def navigate_to_url(self, url):
        self.browser.get(url)

    def type_in_element(self, element_xpath, text):
        self.browser.find_element(By.XPATH, element_xpath).send_keys(text)

    def take_full_page_screenshot(self, request):
        self.reports.take_full_page_screenshot(request)

    def click_button(self, button_xpath):
        self.browser.find_element(By.XPATH, button_xpath).click()