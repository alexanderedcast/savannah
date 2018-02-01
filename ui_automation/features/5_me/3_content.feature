# Created by nik-edcast at 1/17/18
Feature: Verify that cards shown under Me - > content
  """
  In this feature I check if created cards shown correctly
  """

  Scenario: Preparation to test
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Content" tab
    And "Delete" all created data

  Scenario: Verify that All created cards are shown
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create all type of content
    And Verify that "All" cards shown

  Scenario: Verify that SmartCards cards are shown
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Content" tab
    And Verify that "SmartCards" cards shown

  Scenario: Verify that Pathways cards are shown
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Content" tab
    And Verify that "Pathways" cards shown

  Scenario: Verify that Journeys cards are shown
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Content" tab
    And Verify that "Journeys" cards shown

  Scenario: Verify that Completed cards are shown
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Content" tab
    And Verify that "Completed" cards shown

  Scenario: Verify that Bookmarked cards are shown
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Content" tab
    And Verify that "Bookmarked" cards shown
    Then Navigate to "ME" page "Content" tab
    And "Delete" all created data






