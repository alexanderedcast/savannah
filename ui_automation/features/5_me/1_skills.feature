# Created by nik-edcast at 1/3/18
Feature: Verify learning interests and expertise

  """
  As like default value of the interest and expertise is 3.
  I will work with this value
  If we have >= 3 Interests/Expertise I removing thru API for testing purpose
  """

  """"""
  Scenario: Verify have many Interests do you have
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number of "Interests"

  Scenario: Verify that you can to add one Learning Interest
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Add" the "Interests"

  Scenario: Verify that you can to delete one Learning Interest
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Delete" the "Interests"

  Scenario: Verify that you can to Add limit Interests
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Add limit" the "Interests"

  Scenario: Verify that you can Delete all Interests
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Delete All" the "Interests"

  """
  Expertise
  """
  Scenario: Verify have many Expertise do you have
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number of "Expertise"

  Scenario: Verify that you can add one Expertise
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Add" the "Expertise"

  Scenario: Verify that you can delete one Expertise
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Delete" the "Expertise"

  Scenario: Verify that you can to Add limit Expertise
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Add limit" the "Expertise"

  Scenario: Verify that you can Delete all Expertise
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Profile" tab
    Then "Delete All" the "Expertise"

x






