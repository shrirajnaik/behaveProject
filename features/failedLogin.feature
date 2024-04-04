Feature: User Story: Failed Login

Scenario: Failed Login
    Given I am on the Demo Login Page
    When I fill the account information for account LockedOutUser into the Username field and the Password field
    And I click the Login Button
    Then I verify the Error Message contains the text "Sorry, this user has been banned."