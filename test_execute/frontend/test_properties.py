from pytest_bdd import scenario
from test_steps.login.login import *
from test_steps.frontend.tabs import *
from test_steps.frontend.properties import *

@scenario("../../test_cases/frontend/properties.feature", "Add New Property form renders all required fields")
def test_renders_all_required_fields(take_full_page_screenshot_wrapper):
    pass