from test_steps.frontend.AbstractFrontend import AbstractFrontend

class PlaywrightPage(AbstractFrontend):
    
    def __init__(self, page):
        self.page = page

    def navigate_to_url(self, url):
        self.page.goto(url)

    def type_in_element(self, element_xpath, text):
        self.page.fill(f"xpath={element_xpath}", text)