Feature: Properties
    Add/Delete/Edit properties that can later be selected for booking a stay

Scenario: Add New Property form renders all required fields
    Given I logged in as 6Properties
    When I navigate to the Properties tab
    Then I verify Star Rating shows Select placeholder