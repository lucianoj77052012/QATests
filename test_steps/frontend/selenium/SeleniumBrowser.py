from test_steps.frontend.AbstractFrontend import AbstractFrontend
from test_steps.frontend.selenium.SeleniumReports import SeleniumReports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

    def verify_element_exists(self, element_xpath):
        try:
            self.browser.find_element(By.XPATH, element_xpath)
            return True
        except NoSuchElementException:
            return False

    def get_dropdown_selected_value(self, dropdown_xpath):
        star_rating_dropdown = Select(self.browser.find_element(By.XPATH, dropdown_xpath))
        return star_rating_dropdown.all_selected_options[0].text #It's a one-element dropdown.