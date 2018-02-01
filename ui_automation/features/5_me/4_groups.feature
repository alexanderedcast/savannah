# Created by nik-edcast at 1/24/18
Feature: Verify options and features for groups
  """
  Verify that you able:
  1. create a group
  2. share content into group
  3. invite users
  4. assigned  content
  5. edit group
  """
  Scenario: Verify that you able to create a group
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Groups" tab
    And Create a new Group

  Scenario: Verify that user able to invite a user to the group
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Groups" tab
    And Invite user to a group




