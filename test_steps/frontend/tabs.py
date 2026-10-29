import pytest
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from test_steps.frontend.locators import Tabs

@when(parsers.parse("I navigate to the {tab} tab"))
def navigate_tab(browser, tab):
    tab_element = browser.find_element(By.XPATH, Tabs.tab.format(tab))
    tab_element.click()