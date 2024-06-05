Feature: Register and Login

Scenario: User registers successfully
  Given I navigate to the Mercury main page
  When the user clicks on the register button
  Then the user should be on the registration page
  When the user enters valid registration details
  And the user submits the registration form
  Then the registration confirmation message is displayed


Scenario: Successful Login
  Given I navigate to the Mercury main page
  When the user enters valid login credentials
  And the user submits the login form
  Then the login confirmation message is displayed
