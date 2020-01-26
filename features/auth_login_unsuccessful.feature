Feature: Unsuccessfully login through hudl portal


  Scenario: Unsuccessful user login
    Given the user loads the website
    Given the user inputs an invalid username and or password
    When the user selects the login button from the login page
    Then the user is prompted with a login error as expected
