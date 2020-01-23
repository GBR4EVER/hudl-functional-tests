Feature: Successfully login through hudl portal


  Scenario: Successful user login
    Given the user has provided an valid username and password
    When the user selects the login button
    Then the user is successfully logged in as expected
    Then the user is routed to the coach home page

  Scenario: Successful user login with remembered password
    Given the user has provided an valid username and password
    When the user selects the remember password box
    When the user selects the login button
    Then the user is successfully logged in as expected
    Then the user is routed to the coach home page
