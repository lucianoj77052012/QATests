from abc import ABC, abstractmethod

class AbstractFrontend(ABC):

    @abstractmethod
    def navigate_to_url(self, url):
        pass

    @abstractmethod
    def type_in_element(self, element_xpath, text): #Method (CSS, XPATH, etc.) could be sent by param as well, but for now all locators are expected to be in XPATH format.
        pass

    @abstractmethod
    def take_full_page_screenshot(self, request):
        pass

    @abstractmethod
    def click_button(self, button_xpath):
        pass

    @abstractmethod
    def verify_element_exists(self, element_xpath):
        pass

    @abstractmethod
    def get_dropdown_selected_value(self, dropdown_xpath):
        pass