from pytest_bdd import scenario
from test_steps.login.login import * #While * is often considered bad practice, I find it very convenient here, as we're being explicit we want every step we defined there.

@scenario("../../test_cases/login/login.feature", "Login to hotel app")
def test_login():
    pass