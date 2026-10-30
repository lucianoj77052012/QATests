import pytest
import os
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from test_steps.frontend.locators import Properties

@then(parsers.parse("I verify Star Rating shows {placeholder} placeholder"))
def verify_star_rating_select_placeholder(browser, placeholder):
    star_rating_dropdown = Select(browser.find_element(By.XPATH, Properties.star_rating_dropdown))
    star_rating_dropdown_placeholder = star_rating_dropdown.all_selected_options[0].text #It's a one-element dropdown.
    assert star_rating_dropdown_placeholder == placeholder, f"Star Rating dropdown is showing {star_rating_dropdown_placeholder}. Expected: {placeholder}."