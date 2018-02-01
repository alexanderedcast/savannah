# Created by nik-edcast at 12/18/17
Feature: Read a SmartCard
  """Verifying that possible to read all types of cart"""
  """
  1. Login
  2. Create a card
  3. Verify creation
  4. Read a card
  5. Delete a card
  """

  Scenario: Verify that possible to read Link SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Link" card
    And Verify that a card has been created
    Then Verify that possible to read "Link" SmartCard
    And "Delete" a card from your content

  Scenario: Verify that possible to read card from upload - Web Search
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Upload" card
    And Verify that a card has been created
    Then Verify that possible to read "Upload" SmartCard
    And "Delete" a card from your content

  Scenario: Verify that possible to read Text SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then Verify that possible to read "Text" SmartCard
    And "Delete" a card from your content

  Scenario: Verify that possible to read Poll SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Poll" card
    And Verify that a card has been created
    Then Verify that possible to read "Poll" SmartCard
    Then "Delete" a card from your content

  Scenario: Verify that possible to read Quiz SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Quiz" card
    And Verify that a card has been created
    Then Verify that possible to read "Quiz" SmartCard
    Then "Delete" a card from your content




