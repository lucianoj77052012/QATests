from test_steps.frontend.AbstractFrontend import AbstractFrontend

class SeleniumBrowser(AbstractFrontend):
    
    def __init__(self, browser):
        self.browser = browser

    def navigate_to_url(self, url):
        self.browser.get(url)