from pytest_bdd import given, when, then

@given("I create an account")
def login(browser, user):
    username_field = #XPATH
    browser.sendkeys(username_field)
    password_field = #XPATH
    browser.sendkeys(password_field)
    api_key = #Might be addable to the vault.