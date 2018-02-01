# Created by nik-edcast at 1/18/18
Feature: Verify that users from organizations shown correctly

  """
  1. Navigate to Team
  2. Then check if users in UI equal users returned from API
  """

  Scenario: Verify that users under Team > All users shown correctly
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Team" tab
    And Verify users under "All Users" tab


  Scenario: Verify that users under Team > People following me shown correctly
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Team" tab
    And Verify users under "People following me" tab


  Scenario: Verify that users under Team > People I am following shown correctly
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Team" tab
    And Verify users under "People I am following" tab


  Scenario: Verify that users under Team > Subject Matter Experts shown correctly
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Team" tab
    And Verify users under "Subject Matter Experts" tab


  Scenario: Verify that users under Team > Admins shown correctly
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Team" tab
    And Verify users under "Admins" tab


  Scenario: Verify that search under Team return correct results
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Team" tab
    And Verify Search under Me Team

  Scenario: Verify that users under Leaderboard shown correctly
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Leaderboard" tab
    And Verify that user under Leaderboard shown correctly













