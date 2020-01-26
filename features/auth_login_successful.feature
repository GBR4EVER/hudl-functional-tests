Feature: Successfully login through hudl portal


  Scenario: Successful user login
    Given the user loads the website
    Given the user inputs an valid username and password
    When the user selects the login button from the login page
    Then the user is routed to the coach home page as expected

  Scenario: Successful user login with remembered password
    Given the user loads the website
    Given the user inputs an valid username and password
    When the user selects the remember password box
    When the user selects the login button from the login page
    Then the user is routed to the coach home page as expected
