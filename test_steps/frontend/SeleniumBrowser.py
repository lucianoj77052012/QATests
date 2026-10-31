from test_steps.frontend.AbstractFrontend import AbstractFrontend
from selenium.webdriver.common.by import By

class SeleniumBrowser(AbstractFrontend):
    
    def __init__(self, browser):
        self.browser = browser

    def navigate_to_url(self, url):
        self.browser.get(url)

    def type_in_element(self, element_xpath, text):
        self.browser.find_element(By.XPATH, element_xpath).send_keys(text)