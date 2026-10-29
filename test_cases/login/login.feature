Feature: Login
    Verify users are able to login to the hotel app

Scenario: Login to hotel app
    Given I navigated to hotel app link as 6Properties
    When I enter my credentials
    Then I verify the currently active tab is Properties