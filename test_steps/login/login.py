from pytest_bdd import given, when, then

@given("I login as user")
def login(browser, user):
    username_field =
    password_field = 
    browser.sendkeys()
    browser.click(login)