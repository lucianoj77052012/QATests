from pytest_bdd import given, when, then

@given("I navigated to hotel app link")
def login(some_value):
    print(f"Some_value: {some_value}")
    print("Navigated successfully.")
    # username_field =
    # password_field =
    # browser.sendkeys()
    # browser.click(login)