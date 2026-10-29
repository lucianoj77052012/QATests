import pytest
import os
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from test_steps.frontend.locators import Properties