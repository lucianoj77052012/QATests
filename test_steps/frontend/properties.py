import pytest
import os
from pytest_bdd import given, when, then, parsers
from test_steps.frontend.locators import Properties

@then(parsers.parse("I verify Star Rating shows {placeholder} placeholder"))
def verify_star_rating_select_placeholder(frontend, placeholder):
    star_rating_dropdown_placeholder = frontend.get_dropdown_selected_value(Properties.star_rating_dropdown)
    assert star_rating_dropdown_placeholder == placeholder, f"Star Rating dropdown is showing {star_rating_dropdown_placeholder}. Expected: {placeholder}."