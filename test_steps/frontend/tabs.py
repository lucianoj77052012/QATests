import pytest
from pytest_bdd import given, when, then, parsers
from test_steps.frontend.locators import Tabs

@when(parsers.parse("I navigate to the {tab} tab"))
def navigate_tab(frontend, tab):
    frontend.click_button(Tabs.tab.format(tab))